import requests
from bs4 import BeautifulSoup


roland_go_mixer = "https://www.amazon.com/Roland-GO-MIXER-Smartphones-GOMIXERPRO/dp/B07FXBBWNF/ref=sr_1_4?crid=190JT5J5UERL&keywords=roland+go+mixer&qid=1650256807&sprefix=roland+go+mixe%2Caps%2C320&sr=8-4"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


response = requests.get(url=roland_go_mixer, headers=headers)
# print(response.text)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify())

item_name = soup.find(name="span", id="productTitle")
item = item_name.get_text().strip(" ")

price_tag = soup.find(name="span", class_="a-offscreen")
price_float = price_tag.get_text().split('$')[1]

print(f"{item} is now ${price_float}")
