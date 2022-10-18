import random
from flask import Flask, render_template
from datetime import datetime as dt
import requests
from data import DATA

# Get data from API


def get_age_and_gender(name):
    json = {
        'name': name
    }

    response_gender = requests.get("https://api.genderize.io?", params=json)
    response_age = requests.get("https://api.agify.io?", params=json)
    age = response_age.json()['age']
    gender = response_gender.json()['gender']

    return age, gender


app = Flask(__name__)


@app.route('/')
def home():
    ran_num = random.randint(1, 10)
    year = dt.now().year
    return render_template("index.html",
                           num=ran_num,
                           year=year
                           )


@app.route('/guess/<string:name>')
def guess(name):
    result = get_age_and_gender(name)
    age = result[0]
    gender = result[1]
    return render_template("index_guess.html",
                           name=name.title(),
                           gender=gender,
                           age=age
                           )


@app.route('/Blog')
def get_blog():
    return render_template('blog.html', topics=DATA)


if __name__ == "__main__":
    app.run(debug=True)
