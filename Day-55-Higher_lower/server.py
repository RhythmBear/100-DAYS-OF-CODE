from flask import Flask
from random import randint
app = Flask(__name__)

answer = randint(0, 9)
print(answer)


@app.route('/')
def home_page():
    return "<h1>GUESS A RANDOM NUMBER FROM 0 - 9</h1> " \
           "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"


@app.route('/<int:num>')
def answer_page(num):

    if num > answer:
        return "<h1>TOO HIGH, TRY AGAIN</h1> " \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif num < answer:
        return "<h1>TOO LOW, TRY AGAIN</h1> " \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"

    elif num == answer:
        return "<h1>CORRECT YOU FOUND ME</h1> " \
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

app.run(debug=True)

