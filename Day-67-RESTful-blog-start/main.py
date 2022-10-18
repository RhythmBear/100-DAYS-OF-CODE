from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

print('hi')

# # Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# #CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# #WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    # Load posts from Database
    all_posts = BlogPost.query.all()

    return render_template("index.html", all_posts=all_posts)


@app.route('/make_post', methods=['POST', 'GET'])
def make_new_post():
    new_form = CreatePostForm()

    if request.method == "POST" and new_form.validate_on_submit():
        print(new_form.title.data)
        new_post = BlogPost(title=new_form.title.data,
                            subtitle=new_form.subtitle.data,
                            date=datetime.now().strftime("%B %d, %Y"),
                            body=new_form.body.data,
                            author=new_form.author.data,
                            img_url=new_form.img_url.data

                            )
        print(new_post)

        db.session.add(new_post)
        db.session.commit()

        return redirect('/')

    return render_template('make-post.html',
                           form=new_form)


@app.route('/edit_post/<post_id>', methods=["POST", "GET"])
def edit_post(post_id):
    post_to_be_edited = BlogPost.query.get(int(post_id))
    new_form1 = CreatePostForm(
        title=post_to_be_edited.title,
        subtitle=post_to_be_edited.subtitle,
        body=post_to_be_edited.body,
        author=post_to_be_edited.author,
        img_url=post_to_be_edited.img_url

    )

    if request.method == "POST" and new_form1.validate_on_submit():
        post_to_be_edited.title = new_form1.title.data
        post_to_be_edited.subtitle = new_form1.subtitle.data
        post_to_be_edited.date = datetime.now().strftime("%B %d, %Y")
        post_to_be_edited.body = new_form1.body.data
        post_to_be_edited.author = new_form1.author.data
        new_form1.subtitle.img_url = new_form1.img_url.data
        db.session.commit()

        return redirect('/')

    return render_template('make-post.html', form=new_form1)


@app.route("/post/<int:index>")
def show_post(index):
    all_posts = BlogPost.query.all()
    requested_post = None
    for blog_post in all_posts:
        print(blog_post.id)
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/delete/<post_id>')
def delete_post(post_id):
    post = BlogPost.query.get(int(post_id))
    db.session.delete(post)
    db.session.commit()

    all_posts = BlogPost.query.all()
    return render_template('index.html', all_posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
            port=4000,
            debug=True
            )