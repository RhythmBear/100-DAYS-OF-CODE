from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

COOKIE_ENDPOINT = 'https://orteil.dashnet.org/experiments/cookie/'

service = Service("chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(COOKIE_ENDPOINT)


# --------------------Functions--------------------------------------------------#


# Get a dictionary of all the cookie upgrades and their prices
def get_upgrades_dict():
    upgradess = driver.find_elements(by="css selector", value="body div div div div b")

    upgrade_list = [upgrade.text for upgrade in upgradess]
    print(upgrade_list)
    upgrade_dict = {}

    for item in upgrade_list:
        if len(item) < 1:
            continue
        name = item.split(' - ')[0]
        price = item.split(' - ')[1]
        if "," in price:
            price_mod = price.replace(',', '')
        else:
            price_mod = price

        upgrade_dict[name] = int(price_mod)

    return upgrade_dict


def check_for_available_items(upgrades_dictionary: dict):
    for item in upgrades_dictionary:
        output_list = []
        price = upgrades_dictionary[item]
        if score > price:
            output_list.append(price)
        elif score < price:
            break
        return output_list


def get_item_to_buy(available_items):
    if len(available_items) == 0:
        return None

    last_item_price = available_items[-1]
    print(f"THE last item price is {last_item_price}")

    for item in upgrades:
        price = upgrades[item]
        print(price)
        if price == last_item_price:
            to_buy = item
            item_to_buy = f"buy{to_buy}"
            break
        else:
            item_to_buy = None

    return item_to_buy


# ------------------------------------------------------------------------------------#
cookie_button = driver.find_element(by="id", value="cookie")

timeout = 20   # [seconds]
timeout_start = time.time()


while time.time() < timeout_start + timeout:
    cookie_button.click()

# Check how many cookies we have
cookies = driver.find_element(by='id', value="money").text
print(cookies)
cookie_score = cookies

if "," in cookie_score:
    score = cookie_score.replace(',', '')
else:
    score = cookie_score

score = int(cookie_score)
print(score)

upgrades = get_upgrades_dict()
print(upgrades)

# Check which of the items we can buy with the amount of cookies we have
avail_items = check_for_available_items(upgrades_dictionary=upgrades)
print(f"these prices are available {avail_items}")

upgrade_to_get = get_item_to_buy(avail_items)

print(upgrade_to_get)

new_upgrade = driver.find_element(by='id', value=upgrade_to_get)
new_upgrade.click()

cookie_score = driver.find_element(by='id', value="money")
cookie_per_second = driver.find_element(by='id', value="cps")


print(f"Score: {cookie_score.text}")
print(cookie_per_second.text)
