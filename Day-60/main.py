from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form
        print(username)
        password = request.values['Password']
        return f"<h1> Username: {username} Password: {password} </h1> "

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
