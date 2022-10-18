from flask import Flask, render_template
from data import DATA

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", topics=DATA)


@app.route('/<int:id>')
def open_blog(id):
    ind = id - 1
    post = DATA[ind]
    return render_template('post.html', topic=post)


if __name__ == "__main__":
    app.run(debug=True)
