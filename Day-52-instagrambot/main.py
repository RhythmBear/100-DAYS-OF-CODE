import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

IG_URL = 'https://www.instagram.com/'
IG_USERNAME = os.environ['IG_USERNAME']
IG_PASSWORD = os.environ['IG_PASSWORD']
TARGET_ACCOUNT = "koko_rosjares"


class InstagramFollowerBot:
    """
    Logs into Instagram to the Target Instagram account
    """
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('chromedriver/chromedriver.exe'))

    def login(self):
        """This function logs into the instagram account """
        # Open Instagram Website
        self.driver.get(f"{IG_URL}{TARGET_ACCOUNT}")

        # Type in Username
        time.sleep(20)
        try:
            user_name = self.driver.find_element(by='name',
                                                 value='username')
            user_name.send_keys(IG_USERNAME)
        except NoSuchElementException:
            print("failed to locate username")

        # Type in password
        try:
            password = self.driver.find_element(by='name',
                                                value='password')
            password.send_keys(IG_PASSWORD)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("failed to locate password")

        # Disable Notifications

        try:
            notif_button = self.driver.find_element(by='xpath',
                                                    value='/html/body/div[4]/div/div/div/div[3]/button[2]')
            notif_button.click()
        except NoSuchElementException:
            print("failed to locate notif_button")

        # Don't Save login info
        time.sleep(20)
        try:
            d_save = self.driver.find_element(by='xpath',
                                                 value='//*[@id="react-root"]/section/main/div/div/div/div/button')
            d_save.click()
        except NoSuchElementException:
            print("Failed to find Don't save button")

    def print_title(self):
        """Prints the actual name of the Account that is being targeted"""
        time.sleep(10)

        try:
            user = self.driver.find_element(By.TAG_NAME, 'h2')
            print(user.text)
        except NoSuchElementException:
            print("failed to locate h2 tag")

    def search(self):

        """
        The search function searches for an instagram account and selects the first item on the results list
        This function should not be used when logging into with a targeted account
        """
        try:
            search_button = self.driver.find_element(by='xpath',
                                                     value='//*[@id="react-root"]/section/nav/div[2]'
                                                           '/div/div/div[2]/input')

            search_button.send_keys(TARGET_ACCOUNT)
        except NoSuchElementException:
            print("failed to locate search button")

        # Find Popped up account
        try:
            searched = self.driver.find_element(by='xpath',
                                                value='//*[@id="react-root"]/section/nav/div[2]/'
                                                      'div/div/div[2]/div[3]/div/div[2]/div/div[1]/a'
                                                )
            searched.find_element(by='xpath',
                                  value=''
                                  )
        except NoSuchElementException:
            print("failed to locate Searched username")

    def click_followers(self):
        """
        Clicks the followers button on the account page to get a pop-up off all the targeted user's followers

        :return:
        """

        time.sleep(10)
        follower_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_button.click()

    def scroll(self):
        """"
        This function scrolls down on the followers pop-up

        """

        time.sleep(15)

        # TRy to find scrollable window
        try:
            scrollable_popup = self.driver.find_element(By.XPATH,
                                                        '/html/body/div[6]/div/div/div/div[2]')
        except NoSuchElementException:
            try:
                scrollable_popup = self.driver.find_element(By.CLASS_NAME, 'isgrP')
            except NoSuchElementException:
                print("Unable to find scrollable window")
                return False

        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
        time.sleep(2)

    def follow_user(self, follower_index: int):
        """Follows the User and Prints the result of the outcome in the format 'Just followed new_user' """

        time.sleep(5)
        index = follower_index + 1
        x_path = f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[{index}]'
        # user   f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[4]/div/div[1]/div[2]/div[1]/span/a/span'
        # user 2 f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a/span'
        x_path_button = f'{x_path}/div/div[3]/button'
        x_path_button_text = f'{x_path}/div/div[3]/button/div'
        x_path_username = f'{x_path}/div/div[2]/div[1]/div/div/span/a/span'

        follow_button = self.driver.find_element(By.XPATH,
                                                 x_path_button)
        follow_button_text = self.driver.find_element(By.XPATH,
                                                      x_path_button_text)
        user_name = self.driver.find_element(By.XPATH,
                                             x_path_username)

        if follow_button_text.text == 'Follow':
            follow_button.click()
            print(f"Followed {user_name.text}")


bot = InstagramFollowerBot()
bot.login()
bot.print_title()
bot.click_followers()
for i in range(7):
    bot.follow_user(i)

result = bot.scroll()
print(result)
