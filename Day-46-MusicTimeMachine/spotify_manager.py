import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint
import json

SPOTIPY_CLIENT_ID = "7c36e2f9636743cc8ff500f2244aa02f"
SPOTIPY_CLIENT_SECRET = "51ab6fba54bb440dbd7975afc8a590f5"
SPOTIPY_REDIRECT_URL = "https://example.com"

scope = "playlist-modify-private playlist-modify-private"

auth_manager = SpotifyOAuth(scope=scope,
                            client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URL,
                            cache_path="token.txt",
                            )

access_token = auth_manager.get_access_token(as_dict=True)
token = access_token['access_token']
print(token)
sp = spotipy.Spotify(auth=token)
user_details = (sp.current_user())
print(user_details)
user_id = user_details['id']


def get_spotify_object(song_name, year, artist):
    """
    Takes in a Song name and Song Year and Returns a Dictionary containing the song name, artist,
    spotify link and uri for locating it.

    """
    global sp, auth_manager, scope

    search_result = sp.search(q=f"track:{song_name} year:{year}", limit=5, type="track")
    # pprint.pprint(search_result)

    # Get Url for Song
    try:
        result_from_api = search_result["tracks"]["items"][0]

    except IndexError:
        print(f"No details found for this track {song_name} by {artist}")

        return "None"
    else:
        song_url = result_from_api['uri']
        song_name = result_from_api["name"]
        song_artist = result_from_api['artists'][0]['name']
        spotify_link = result_from_api["external_urls"]["spotify"]

        output_dic = {
            "song_name": song_name,
            "song_artist": song_artist,
            "song_url": song_url,
            "spotify_link": spotify_link,
        }

        return output_dic


song_list = []
author_list = []

# Opening Previously created Json file from Data Scrapped from the Billboard.com website
with open("Billboard_2010-10-10_data.json") as file:
    song_json = json.load(file)
    print(song_json)

    for item in song_json:
        # Extracting Song Name and Author name from the json file created

        song_title = song_json[item]['Song name']
        author_name = song_json[item]['Author Name']

        # Appending song name and Author name to list
        song_list.append(song_title)
        author_list.append(author_name)

print(song_list)
print(author_list)
song_urls = []

for i in range(10):
    song = song_list[i]
    artist = author_list[i]
    result = get_spotify_object(song_name=song, year="2010", artist=artist)
    # print(result)
    if result == "None":
        continue
    uri = result["song_url"]
    song_urls.append(uri)

# result = get_spotify_object(song_name="I like it", year="2018")
# print(result)
#


# Creates New playlist
new_playlist = sp.user_playlist_create(user=user_id,
                                       name="Sample Playlist",
                                       public=False,
                                       description="Playlist Created to test Time Machine code",
                                       collaborative=True
                                       )
print(new_playlist)
playlist_id = new_playlist['id']
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_urls)



























