from bs4 import BeautifulSoup
import requests
import re
from selenium.webdriver import Chrome
import time


driver = Chrome("C:/Users/EMMANUEL/Downloads/chromedriver_win32/chromedriver.exe")

driver.get('https://www.empireonline.com/movies/features/best-movies-2/')

element = driver.find_element(by="h3")

movies_website = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=movies_website)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

title = soup.title.text
print(title)

h3_tags = soup.find(name="h3")

print(h3_tags)