from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

WIKI_PAGE = 'https://en.wikipedia.org/wiki/Main_Page'
SIGNUP_PAGE = "https://secure-retreat-92358.herokuapp.com/"

service = Service(executable_path="chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
#
# driver.get(WIKI_PAGE)
#
# article_count = driver.find_element(by="css selector", value="#articlecount a")
# print(article_count.text)
# article_count.click()
#
#
# search = driver.find_element(by="name", value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
#
# time.sleep(15)

driver.get(SIGNUP_PAGE)

fname = driver.find_element(by="name", value="fName")
fname.send_keys("Emmanuel")
lname = driver.find_element(by="name", value="lName")
lname.send_keys("Adepoju")
email = driver.find_element(by="name", value="email")
email.send_keys("eoadepoju10@gmail.com")

submit = driver.find_element(by="xpath", value="/html/body/form/button")
submit.click()

time.sleep(10)



driver.quit()
