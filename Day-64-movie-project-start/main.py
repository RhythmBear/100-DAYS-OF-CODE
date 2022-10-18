from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from requests.exceptions import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
# Create Database
db = SQLAlchemy(app)


# ---------------------------------------------- CLASSES AND FUNCTIONS -----------------------------------------------#
# -----------------------------CLASSES ------------------------------------ #
# Create Database Model for Movies
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True)


# Form Class for Changing Rating and Review
class EditForm(FlaskForm):
    new_rating = StringField('Your rating Out of 10(e.g 8.5)', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])

    submit = SubmitField('Submit')


# CLass for adding NEw MOvie to the Database
class AddMovieForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Search Movie')


# CLASS FOR STRUCTURING THE MOVIES COLLECTED FROM THE TMDB API
class MovieResult:

    def __init__(self):
        self.title = None
        self.image_url = None
        self.release_year = None
        self.description = None


# ----------------------------FUNCTIONS -------------------------------------------#
def get_movie_data(movie_title):
    """
    This Function returns a list of movie search results objects containing title, image_url
    release_year and description
    :param movie_title:
    :return:
    """

    IMDB_URL = "https://api.themoviedb.org/3/search/movie"
    MY_API_KEY = '65a5105bc82941f1ea08c5efe726d580'
    MOVIE_RESULT_LIST = []
    img_base_url = 'https://image.tmdb.org/t/p/w342'

    parameters = {
        'api_key': MY_API_KEY,
        'query': movie_title,
    }

    try:
        response = requests.get(url=IMDB_URL, params=parameters)
        response.raise_for_status()

    except ConnectTimeout or ConnectionError:
        return []

    else:
        data = response.json()
        if len(data['results']) == 0:
            return []

    for result in data['results']:
        movie_item = MovieResult()
        movie_item.title = result['original_title']
        url = result['poster_path']

        # Since there is a possibility that the url returns a None type we Have to account for that

        if result['poster_path']:
            movie_item.image_url = img_base_url + result['poster_path']
        else:
            if result['backdrop_path']:
                movie_item.image_url = img_base_url + result['backdrop_path']
            else:
                movie_item.image_url = img_base_url

        movie_item.description = result['overview']
        movie_item.release_year = result['release_date']

        MOVIE_RESULT_LIST.append(movie_item)

    return MOVIE_RESULT_LIST


def change_rating_and_review(rating, review, item_id):
    movie_to_update = Movies.query.get(item_id)
    movie_to_update.review = review
    movie_to_update.rating = rating
    db.session.commit()


def add_rank(rank, item_id):
    movie_to_update = Movies.query.get(item_id)
    movie_to_update.ranking = rank
    db.session.commit()


def del_movie(item_id):
    movie_to_delete = Movies.query.get(item_id)
    db.session.delete(movie_to_delete)
    db.session.commit()


def add_movie(movie_title, movie_year, movie_desc, movie_img_url):
    """
    This Function adds a new movie to the database and returns the movie from the database as the output.
    so that the movies details can be accessed.
    :param movie_title:
    :param movie_year:
    :param movie_desc:
    :param movie_img_url:
    :return:
    """
    movie_to_be_added = Movies(title=movie_title,
                               year=movie_year,
                               description=movie_desc,
                               img_url=movie_img_url
                               )
    db.session.add(movie_to_be_added)
    db.session.commit()

    current_movie = Movies.query.filter_by(title=movie_title).first()

    return current_movie


# -------------------------------------------------------------------------------------------------------------- #
db.create_all()

new_movie = Movies(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
                "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads "
                "to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)


# --------------------------------------- ROUTES ------------------------------------- #

# I created this variable to link the search_movie and select_movie route.
search_results = []


@app.route("/")
def home():
    # db.session.add(new_movie)
    # db.session.commit()
    ordered_movies = db.session.query(Movies).order_by(Movies.rating.desc()).all()
    rank = 1
    for movie in ordered_movies:
        add_rank(rank=rank, item_id=movie.id)
        rank += 1

    movies_db = Movies.query.all()
    print(movies_db)
    return render_template("index.html", movies=ordered_movies)


@app.route('/ADD', methods=['GET', 'POST'])
def search_movie():
    # Route for getting movie to be added to Database.
    global search_results
    new_movie_form = AddMovieForm()

    if request.method == "POST" and new_movie_form.validate_on_submit():
        search_item = new_movie_form.movie_title.data

        search_results = get_movie_data(movie_title=search_item)

        return render_template('select.html', movie_results=search_results)

    return render_template('add.html',
                           movieform=new_movie_form
                           )


@app.route('/edit<movie_num>', methods=['POST', 'GET'])
def edit_movie(movie_num):
    new_form = EditForm()
    movie_to_be_edited = Movies.query.get(int(movie_num))

    if request.method == 'POST' and new_form.validate_on_submit():
        print(new_form.new_rating.data)
        print(new_form.new_review.data)
        change_rating_and_review(rating=new_form.new_rating.data,
                                 review=new_form.new_review.data,
                                 item_id=int(movie_num)
                                 )
        return redirect('/')

    return render_template('edit.html',
                           movie_mod=movie_to_be_edited.title,
                           form=new_form)


@app.route('/select-<mv_index>')
def select_movie(mv_index):
    print(mv_index)
    print(search_results)
    if len(search_results) > 0:
        movie_data = search_results[int(mv_index)]
        movie_that_was_added = add_movie(movie_title=movie_data.title,
                                         movie_year=movie_data.release_year,
                                         movie_desc=movie_data.description,
                                         movie_img_url=movie_data.image_url
                                         )

        # Since the movie that was added returns the movie details we can now target its id and send
        # it through the edit page for editing
        print(movie_that_was_added.id)

        return redirect(f'/edit{movie_that_was_added.id}')

    return redirect('/')


@app.route('/delete<movie_id>')
def delete(movie_id):
    del_movie(movie_id)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
