import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from pprint import pprint

GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdHPylxV1L-BJbSD8D06cQshoKBBIiYZPRTqxd7XRRUzQGf5w/viewform'
CHROME_DRIVER = "chromedriver/chromedriver.exe"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22users" \
             "SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east" \
             "%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%" \
             "22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%" \
             "7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%" \
             "7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%" \
             "22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C" \
             "%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22" \
             "%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

address = 'list-card-addr'
price = 'list-card-price'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


class ZillowScraper:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER))
        self.driver.get(ZILLOW_URL)
        options = ChromeOptions()
        options.headless = True
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.result_dict = []

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_house_cards(self):
        time.sleep(15)
        cards = self.soup.find_all(name='div', class_='list-card-info')
        no_of_results = len(cards)
        print(no_of_results)

        for card in cards:
            pprint(card)

            if card is None:
                continue

            # Try to get card link
            try:
                # print(card.a['href'])
                card_link = card.a['href']
            except TypeError or AttributeError:
                print("This card does not contain housing details")
                continue
            else:
                if card_link[:5] != 'https':
                    card_link_ = f"https://www.zillow.com{card_link}"
                    print(card_link_)
                else:
                    card_link_ = card_link

            # Try to get card address
            try:
                card_address = card.a.address.text

            except AttributeError or TypeError:
                card_address = card.find(name='address', class_='list-card-addr').text

            # Try to get card price
            try:
                card_price = card.find(name='div', class_='list-card-price').text
            except AttributeError or TypeError:
                print("could not locate card price")
                continue

            result_dict = {'link': card_link_, 'address': card_address, 'price': card_price}
            print(result_dict)

            self.result_dict.append(result_dict)

        return self.result_dict

    def fetch_address(self):
        addresses = self.soup.find_all(name='address', class_=address)

        address_list = []

        for item in addresses:
            address_list.append(item.text)

        return address_list

    def fetch_prices(self):
        prices = self.soup.find_all(name='div', class_='list-card-price')

        price_list = []

        for item in prices:
            price_list.append(item.text)

        return price_list


class FormData:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER))
        self.driver.get(url=GOOGLE_FORM_URL)

    def go_back(self):
        self.driver.back()

    def update_form(self, house_price, house_address, house_link):
        time.sleep(20)
        # FInd the price input
        try:
            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                             '/div/div[1]/div/div[1]/input')
        except NoSuchElementException:
            print("Failed to locate price input")
            return None

        else:
            price_input.send_keys(house_price)

        # Find address input
        try:
            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                           '/div/div[1]/div/div[1]/input')
        except NoSuchElementException:
            print("Failed to locate the address input")
        else:
            address_input.send_keys(house_address)

        # FInd the link input button
        try:
            link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                        '/div/div[1]/div/div[1]/input')
        except NoSuchElementException:
            print("Failed to find the requested button ")
        else:
            link_input.send_keys(house_link)

        try:
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        except NoSuchElementException:
            print("Couldn't find submit button")
        else:
            time.sleep(30)
            submit_button.click()

    def check_form_submission(self):
        time.sleep(10)
        result = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]')
        print(result)
