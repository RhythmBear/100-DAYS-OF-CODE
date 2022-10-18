from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

ADMIN_ID = "administrator"
ADMIN_PASS = "administrator"


app = Flask(__name__)
app.secret_key = "secretkey"
Bootstrap(app)


class LoginForm(FlaskForm):
    # What's happening here is that we are creating a new form item called username that has as leas
    # and is also labelled username. It must be at least 8 characters in length and must not be more than 30
    # The message Argument is the message that is returned if the conditions are not met
    username = StringField(label='Username',
                           validators=[DataRequired()])

    password = StringField(label='Password',
                           validators=[DataRequired()])
    login = SubmitField('Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Creates new Form from the class created up
    msg = None
    new_form = LoginForm()

    # Checks if the submit button has been pressed and if the details entered passed the vibe check
    if request.method == 'POST' and new_form.validate_on_submit():
        print(new_form.username.data, new_form.password.data)

        if new_form.username.data == ADMIN_ID and new_form.password.data == ADMIN_PASS:
            msg = True
            return render_template('success.html')

        else:
            return render_template('denied.html')

    return render_template('login.html', form=new_form, message=msg)


if __name__ == '__main__':
    app.run(debug=True)
