from bs4 import BeautifulSoup
import requests


def scrape_billboard(date):

    """
    Scrapes the billboard website and returns a Nested list of the songs list and authors lists
    Also creates a Json file with the data
    """

    # Getting the Webpage with the specified date to the response variable

    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    webpage = response.text

    # Creating soup object to scrape data from website
    soup = BeautifulSoup(webpage, "html.parser")
    # print(soup.prettify())

    title = soup.find(name="h3", id="title-of-a-story")


    # print(title)
    song_list = soup.select(selector="li ul li h3")
    author_list = soup.select(selector="li ul li span")

    # print(song_list)

    list_of_songs = []
    list_of_authors = []

    num = 1
    for element in song_list:
        for song_title in element.stripped_strings:
            # print(f"{num}) {song_title}")
            list_of_songs.append(song_title)
            num += 1

    num = 1
    for element in author_list:
        for author in element.stripped_strings:
            x = (num + 6) % 7
            if x != 0:
                num += 1
                continue
            else:
                y = (num + 6) / 7
                y = str(int(y))

                # print(f"{y}) {author} ")
                list_of_authors.append(author)
                num += 1

    output_dict = [list_of_songs, list_of_authors]
    return output_dict
