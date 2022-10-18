from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)

gravatar = Gravatar(app,
                    size=20,
                    rating='x',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

Base = declarative_base()

# #CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def login_manager(user_id):
    return User.query.get(int(user_id))


# CONFIGURE TABLES

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)

    # Builds a relationship with the User class
    author = db.relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Builds a relationship with the Comment class
    comments = db.relationship("Comment", back_populates="comment_post")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)

    # relationship with the posts class and comments class
    posts = db.relationship("BlogPost", back_populates="author")
    comments = db.relationship("Comment", back_populates="comment_author")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    comment_user_id = db.Column(db.Integer, ForeignKey('users.id'))
    comment_author = db.relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, ForeignKey('blog_posts.id'))
    comment_post = db.relationship("BlogPost", back_populates="comments")


db.create_all()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html",
                           all_posts=posts,
                           user=current_user)


@app.route('/register', methods=["POST", "GET"])
def register():
    new_register_form = RegisterForm()

    if request.method == "POST" and new_register_form.validate_on_submit():
        print(new_register_form.email.data)

        # Checks to see if the User details entered, already exists in our database
        user_exists = User.query.filter_by(email=new_register_form.email.data).first()
        print("search Complete")
        if user_exists:
            flash(message=f"{new_register_form.email.data} is already registered.\nTry Logging in.",
                  category="email_registered")

            return redirect(url_for('login'))

        else:
            hashed_password = generate_password_hash(password=new_register_form.password.data,
                                                     method='pbkdf2:sha256',
                                                     salt_length=8)

            new_user = User(email=new_register_form.email.data,
                            password=hashed_password,
                            name=new_register_form.name.data)


            db.session.add(new_user)
            db.session.commit()
            flash(message="Successfully Registered. Please Log in with your details", category="register_success")

            return redirect(url_for('login', logged_in=new_user.is_authenticated))

    return render_template("register.html", form=new_register_form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()


    if current_user.is_authenticated:
        return redirect(url_for('get_all_posts'))

    if request.method == "POST" and login_form.validate_on_submit():
        user_exists = User.query.filter_by(email=login_form.email.data).first()

        if user_exists:
            password = user_exists.password
            password_correct = check_password_hash(pwhash=password,
                                                   password=login_form.password.data)

            if password_correct:
                login_user(user_exists)

                flash(message="Login Successful", category="login_success", )

                return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))
            else:
                flash(message="Password Incorrect",
                      category="incorrect_password")

                return redirect(url_for('login'))

        else:
            flash(message="Username is Incorrect", category="incorrect_username")

            return redirect(url_for('login', logged_in=current_user.is_authenticated))

    return render_template("login.html",
                           form=login_form,
                           logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(int(post_id))
    print(requested_post)
    requested_comments = Comment.query.filter_by(post_id=int(post_id)).all()

    new_comment_form = CommentForm()
    if request.method == "POST" and new_comment_form.validate_on_submit():
        users_comment = new_comment_form.comment.data
        new_comment = Comment(
            text=new_comment_form.comment.data,
            comment_author=current_user,
            comment_post=requested_post
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))

    return render_template("post.html", comments=requested_comments,
                           c_form=new_comment_form,
                           post=requested_post,)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=['GET', 'POST'])
@login_required
def add_new_post():
    if current_user.id != 1:
        return redirect(url_for('get_all_posts'))
    form = CreatePostForm()
    if form.validate_on_submit() and request.method == "POST":
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect (url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=['POST', 'GET'])
@login_required
def edit_post(post_id):

    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit() and request.method == 'POST':
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, user=current_user)


@app.route("/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
