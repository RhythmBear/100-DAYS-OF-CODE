from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


LINKEDIN = "https://www.linkedin.com/jobs/?showJobAlertsModal=false"
LINKEDIN_JOB = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
LINKEDIN_USERNAME = "eoadepoju10@gmail.com"
LINKEDIN_PASSWORD = "Okechukwu10."

service = Service("chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(LINKEDIN_JOB)

sign_in_button = driver.find_element(by="xpath", value="/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

email = driver.find_element(by="xpath", value='//*[@id="username"]')
email.send_keys(LINKEDIN_USERNAME)

password = driver.find_element(by="xpath", value='//*[@id="password"]')
password.send_keys(LINKEDIN_PASSWORD)

login = driver.find_element(by='xpath', value='//*[@id="organic-div"]/form/div[3]/button')
login.click()

time.sleep(10)

#
# driver.quit()