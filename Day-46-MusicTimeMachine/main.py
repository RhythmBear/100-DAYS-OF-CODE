import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from art import shuttle
from datetime import datetime as dt
from webscraper import scrape_billboard
from functions import *

# Collect date user would like to travel to via user input.
# print(shuttle)
print("Welcome to the Music Time machine 🚀 \nThis takes to back to a particular date through a spotify playlist of the songs that were trending then.")

print("What year would you like to travel to?")
year_input = int(input("\nYear(e.g 2022): "))
month_input = int(input("\nWhat month in that year(e.g 08): "))
day_input = int(input("\nDay(e.g 12): "))
amount = int(input("How many songs will you like to get from that year(minimum of 15 max of 90): ")) + 5
print("\nCollecting user details...\n")

date = dt(year=year_input, month=month_input, day=day_input)
print(f"Preparing Shuttle to take you to {date}")
date = date.date()

# Scrape billboard and get song and author list using the date collected from user
print("\nScraping Billboard for song Titles...\n")
response = scrape_billboard(date=date)
song_list = response[0]
author_list = response[1]

# Edit Song Names and author names.
print("\nEditing and fine tuning song and artist names...\n")
edited_song_list = remove_strange_characters(titles=song_list)
edited_author_list = remove_featuring(remove_strange_characters(titles=author_list))

# result = get_spotify_object(song_name="i like it", year="2020")
# print(result)
#

# -----------------------------------------SPOTIFY ----------------------------------------------------------#

print("\nAuthenticating with Spotify...\n")
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
# print(token)

sp = spotipy.Spotify(auth=token)
user_details = (sp.current_user())
# print(user_details)

user_id = user_details['id']


def get_spotify_object(song_name, year, artist):
    """
    Takes in a Song name and Song Year and Returns a Dictionary containing the song name, artist,
    spotify link and uri for locating it.

    """
    global sp, auth_manager, scope

    search_result = sp.search(q=f"track:{song_name} year:{year} artist:{artist}", limit=5, type="track")
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

print("\nGetting song links...\n")
# print(song_list)
# print(author_list)
song_urls = []

for i in range(amount):
    song = edited_song_list[i]
    artist = edited_author_list[i]
    result = get_spotify_object(song_name=song, year=str(year_input), artist=artist)
    # print(result)
    if result == "None":
        continue
    uri = result["song_url"]
    song_urls.append(uri)

# result = get_spotify_object(song_name="I like it", year="2018")
# print(result)
#

print("\nCreating Platlist...\n")
# Creates New playlist
new_playlist = sp.user_playlist_create(user=user_id,
                                       name=f"Memories from {date}",
                                       public=False,
                                       description=f"Playlist created by Emmanuel's Music Time machine to take "
                                                   f"you back in time to {date} through the power of music. ",
                                       collaborative=False
                                       )
print(new_playlist)
playlist_id = new_playlist['id']

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_urls)

try:
    playlist_link = new_playlist["external_urls"]['spotify']
except KeyError:
    print("Oops! I'm sorry an error occured and we failed to create the Playlist, PLease Contact Admin.")
else:
    print(f"\n\nThanks for using our service \nHere's the link your Playlist: {playlist_link}")
