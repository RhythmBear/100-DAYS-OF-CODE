from flask import Flask, render_template, request
import requests
from mailer import send_email
from pprint import pprint

response = requests.get('https://api.npoint.io/1c809362b23debb994b1')
posts_json = response.json()


app = Flask(__name__)


@app.route('/')
def home_page():

    return render_template("index.html", blog_posts=posts_json)


@app.route('/About')
def about():
    return render_template("about.html")


@app.route('/Contact', methods=['GET', 'POST'])
def contact_me():
    # Checks method tomake sure its post
    if request.method == "POST":
        # Retrieve Form response if a post was made
        print(request.form)
        result = send_email(name=request.form['name'],
                            email_adr=request.form['email'],
                            phone_number=request.form['phone'],
                            message=request.form['message']
                            )
        print(result)
        return render_template("contact.html",
                               contact_message="Your Message has been sent!")

    else:
        # Return the regular contact me message if no post request was made
        return render_template("contact.html",
                               contact_message="CONTACT ME")


@app.route('/<ind>')
def post(ind):

    id = int(ind)
    title = posts_json[id]['title']
    subtitle = posts_json[id]['subtitle']
    body = posts_json[id]['body']

    return render_template('post.html',
                           post_title=title,
                           post_subtitle=subtitle,
                           post_body=body)


if __name__ == "__main__":
    app.run(debug=True)
