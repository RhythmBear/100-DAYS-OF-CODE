import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

ZILLOW_URL = 'https://www.zillow.com/homes/California_rb/'
CHROME_DRIVER = "chromedriver/chromedriver.exe"

driver = webdriver.Chrome(service=Service(CHROME_DRIVER))
driver.get(ZILLOW_URL)


soup = BeautifulSoup(driver.page_source, 'html.parser')
cards = soup.find_all(name='div', class_='list-card-info')
print(len(cards))

time.sleep(20)

for card in cards:
    print(card)

    if card is None:
        continue
    try:
        print(card.a['href'])
    except AttributeError:
        print("This card does not contain housing details")
        continue

    try:
        print(card.div.address.text)
    except AttributeError:
        print(card.find(name='address', class_='list-card-addr').text)

    price = card.find(name='div', class_='list-card-price').text
    print(price)


