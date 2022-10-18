from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

TINDER_URL = "https://tinder.com/"
TINDER_EMAIL = os.environ['TINDER_EMAIL']
TINDER_PASSWORD = os.environ['TINDER_PASSWORD']

new_service = Service("chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=new_service)

print("running...")

# Open tinder url
driver.get(TINDER_URL)

# Get tabs and close the settings Tab
print(driver.window_handles)
base_tab = driver.window_handles[0]
tinder_window = driver.window_handles[1]
driver.switch_to.window(base_tab)
print(driver.title)
driver.close()

driver.switch_to.window(tinder_window)
time.sleep(10)

# Click Tinder Login Button
sign_in_button = driver.find_element(by="xpath", value='//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
sign_in_button.click()

print("Login button clicked...")
time.sleep(10)

# Click Login through facebook
facebook_but = driver.find_element(by="xpath", value='//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
facebook_but.click()

# Change to the current newly popped up window to log in to facebook.
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])

email = driver.find_element(by="xpath", value='//*[@id="email"]')
email.send_keys(TINDER_EMAIL)

password = driver.find_element(by="xpath", value='//*[@id="pass"]')
password.send_keys(TINDER_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to the regular window and wait for pop-ups to load before trying to click on any buttons
driver.switch_to.window(tinder_window)

time.sleep(25)

try:
    time.sleep(20)
    enable_location = driver.find_element(by="xpath", value='//*[@id="q-789368689"]/div/div/div/div/div[3]/button[1]')
    enable_location.click()
except Exception as e:
    print("Failed to locate location button")
    print(f"Error type: {type(e).__name__} \nline: {e.__traceback__.tb_lineno}")

try:
    time.sleep(20)
    accept_cookie = driver.find_element(by="xpath", value='//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button')
    accept_cookie.click()
except Exception as e:
    print("Failed to accept cookie button")
    print(f"Error type: {type(e).__name__} \nline: {e.__traceback__.tb_lineno}")

try:
    time.sleep(20)
    disable_notif = driver.find_element(by="xpath", value='//*[@id="q-789368689"]/div/div/div/div/div[3]/button[2]')
    disable_notif.click()
except Exception as e:
    print("Failed to locate disable")
    print(f"Error type: {type(e).__name__} \nline: {e.__traceback__.tb_lineno}")

# START REJECTING ALL OFFERS
for i in range(5):
    time.sleep(10)

    try:
        reject_button = driver.find_element(by="xpath",
                                        value='//*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[2]/button')
        reject_button.click()

    except:
        try:
            reject_button = driver.find_element(by="xpath",
                                            value='//*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button')
            reject_button.click()

        except:
            try:
                reject_button = driver.find_element(by="xpath",
                                                    value='//*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[2]/button/span/span')
                reject_button.click()
            except:


                print("Unable to find required cancel button")


home_screen_notif = '//*[@id="q-789368689"]/div/div/div[2]/button[2]'
cancel_home_screen = driver.find_element(by='xpath', value=home_screen_notif)
cancel_home_screen.click()

# //*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[2]/button'
# //*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button
# //*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[2]/button

# login_button = driver.find_element(by="name", value='Login')
# login_button.click()

# driver.quit()
