from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pprint

CHROME_DRIVER = "chromedriver\chromedriver.exe"
GO_MIXER_ENDPOINT = 'https://www.amazon.com/Roland-GO-MIXER-Smartphones-GOMIXERPRO/dp/B07FXBBWNF/ref=sr_1_4?' \
                    'crid=190JT5J5UERL&keywords=roland+go+mixer&qid=1650256807&sprefix=roland+go+mixe%2Caps%2C320&sr' \
                    '=8-4 '
PYTHON_ENDPOINT = "https://www.python.org"

# Setting up selenium

service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=service)

driver.get(PYTHON_ENDPOINT)
# item_name = driver.find_element(by='id', value="productTitle")
# print(item_name.text)

list_number = 1
event_dict = {}

for i in range(5):
    i += 1

    event_name = driver.find_element(by="xpath", value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{list_number}]/a')
    event_date = driver.find_element(by="xpath", value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{list_number}]/time')
    print(f"{event_name.text} holds on {event_date.text}")

    event_dict[i] = {
        "Event Name": event_name.text,
        "Event Date": event_date.text
                     }
    list_number += 1

pprint.pprint(event_dict)

driver.quit()
