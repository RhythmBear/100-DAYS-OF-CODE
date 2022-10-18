import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

TWITTER_URL = "https://twitter.com/"
TWITTER_USERNAME_2 = 'Emmanueladepo17'
TWITTER_PASSWORD = "okechukwu"
TWITTER_USERNAME = "femiemmanuel1990@gmail.com"
SPEED_URL = "https://www.speedtest.net/"
GO_BUTTON_XPATH = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'


class SpeedBot:

    def __init__(self):
        service = Service("chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        print(self.driver)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)

        time.sleep(10)
        go_button = self.driver.find_element(by='xpath',
                                             value=GO_BUTTON_XPATH)
        go_button.click()
        time.sleep(120)
        upload = self.driver.find_element(by="xpath",
                                          value='//*[@id="container"]'
                                                '/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div'
                                                '/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        download = self.driver.find_element(by="xpath",
                                            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                  'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = upload.text
        self.down = download.text

    def enter_password(self):
        time.sleep(60)
        try:
            password = self.driver.find_element(by='xpath',
                                                value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]'
                                                      '/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
                                                )
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            return True

        except NoSuchElementException:
            try:
                password = self.driver.find_element(by="name",
                                                    value='password')
                password.send_keys(TWITTER_PASSWORD)
                password.send_keys(Keys.ENTER)

                return True
            except NoSuchElementException:
                print("Failed to locate password button.")

                return False

    def login(self):
        time.sleep(30)

        login = self.driver.find_element(by="xpath",
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/'
                                               'div/div[3]/div[5]/a')
        login.click()

    def enter_username(self):
        try:
            user_name = self.driver.find_element(by='name', value='text')
            user_name.send_keys(TWITTER_USERNAME_2)
            user_name.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("Did not find username element")

    def enter_email_address(self):
        time.sleep(60)

        try:
            username = self.driver.find_element(by='xpath',
                                                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                      '/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
                                                )
        except NoSuchElementException:
            print("Failed to locate Username button")
            windows = self.driver.window_handles
            print(len(windows))
            username = self.driver.find_element(by='xpath',
                                                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                      '/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
                                                )
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.ENTER)

        else:
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.ENTER)

    def send_tweet(self, message):
        time.sleep(30)
        tweet = self.driver.find_element(by='xpath',
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]'
                                               '/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/'
                                               'div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(message)

        send = self.driver.find_element(by='xpath',
                                        value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]'
                                              '/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send.click()

    def tweet_at_provider(self):
        time.sleep(10)
        self.driver.get(TWITTER_URL)

        # Delete Settings Tab
        print(self.driver.window_handles)
        base_tab = self.driver.window_handles[0]
        twitter_window = self.driver.window_handles[1]
        self.driver.switch_to.window(base_tab)
        print(self.driver.title)
        self.driver.close()

        self.driver.switch_to.window(twitter_window)

        self.login()

        self.enter_email_address()

        result = self.enter_password()

        if not result:
            self.enter_username()
            self.enter_password()

        self.send_tweet(message=f"HEY @SmileComsNGCare Why is my Internet "
                                f"download speed at {self.down}mbps and my upload speed at {self.up}mbps ?")


bot = SpeedBot()
print(bot.up)
print(bot.down)
bot.get_internet_speed()
print(bot.up)
print(bot.down)

bot.tweet_at_provider()
