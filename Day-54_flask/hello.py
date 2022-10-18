from flask import Flask
app = Flask(__name__)


# ---------------- Create HTMl Decorators --------------------- #
def make_bold(function):

    def add_bold_tag():
        word = function()
        return f"<h1><b>{word}</b></h1>"

    return add_bold_tag


def make_italic(function):

    def add_italic_tag():
        word = function()
        return f"<em>{word}</em>"

    return add_italic_tag


def make_underline(function):

    def underline_text():
        word = function()
        return f"<u>{word}</u>"

    return underline_text
# ------------------------------------------------------------------#


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'Bye!'


@app.route('/<string:name>')
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
