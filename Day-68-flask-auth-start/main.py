from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Creating a login manager that loads the user for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
#
# db.create_all()


@app.route('/')
def home():
    print(current_user)
    # Checks to see if the current user in logged in, SO that we do not return the original Login page
    if current_user.is_authenticated:
        return redirect(url_for('secrets', user_id=current_user.id))
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():

    if request.method == "POST":

        email_exists = User.query.filter_by(email=request.form['email']).first()
        print(email_exists)

        if email_exists:
            flash('That Email address is already registered, Please Login', category='info')
            return redirect(url_for('login'))

        else:
            new_user_password = request.form['password']
            hashed_password = generate_password_hash(
                password=new_user_password,
                method='pbkdf2:sha256',
                salt_length=8
            )
            print(hashed_password)

            new_user = User(email=request.form['email'],
                            name=request.form['name'],
                            password=hashed_password
                            )
            print(new_user)

            db.session.add(new_user)
            db.session.commit()
            flash("You have been Successfully Registered, Please Sign in with you Username and Password",
                  category="register")

            return redirect(url_for('login', user=new_user.name))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        # get username and password variables from inputs
        password = request.form['password']
        email = request.form['email']

        # Query the database to get the details that match the email Provided above
        user = User.query.filter_by(email=email).first()
        # Checks if the User with that email exists in the database
        if user:
            # Checks to see if the password Provided is correct.
            password_correct = check_password_hash(user.password, password)
            if password_correct:

                login_user(user)

                flash('Logged in successfully.', category='success')

                print(user.is_authenticated)
                print(user.name)
                # I'm passing the User Object into the html so that I can access a few of its attributes
                return redirect(url_for('secrets', user_id=user.id, logged_in=user.is_authenticated))
            else:
                flash('Incorrect password entered, Try again!', category='password_error')
                return redirect(url_for('login', logged_in=user.is_authenticated))
        else:
            flash('That Email address does not exist, Try Again!', category='email_error')
            return redirect(url_for('login'))

    return render_template("login.html", )


@app.route('/secrets/<user_id>')
@login_required
def secrets(user_id):
    user = User.query.get(user_id)

    return render_template("secrets.html",
                           name=user.name,
                           logged_in=user.is_authenticated
                           )


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
    pass


@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(directory='static/files',
                               filename=filename,
                               as_attachment=True
                               )


if __name__ == "__main__":
    app.run(debug=True, port=4000)
