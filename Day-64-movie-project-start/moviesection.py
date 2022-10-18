import requests
from requests.exceptions import *


# I created a Class that holds the Movie Structure
class MovieResult:

    def __init__(self):
        self.title = None
        self.image_url = None
        self.release_year = None
        self.description = None


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

    for result in data['results']:
        movie_item = MovieResult()
        movie_item.title = result['original_title']
        movie_item.image_url = img_base_url + result['poster_path']
        movie_item.description = result['overview']
        movie_item.release_year = result['release_date']

        MOVIE_RESULT_LIST.append(movie_item)

    return MOVIE_RESULT_LIST


movies = get_movie_data("avengers")
for item in movies:
    print(item.image_url)
