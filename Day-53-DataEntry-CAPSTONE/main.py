import time

from DataManager import ZillowScraper, FormData

zillow = ZillowScraper()
# prices = zillow.fetch_prices()
# addresses = zillow.fetch_address()
time.sleep(20)
zillow.scroll_down()

time.sleep(20)
amount = zillow.get_house_cards()

print(len(amount))

data = zillow.result_dict
print(data)

for item in data:
    print(item['link'])
    print(item['address'])
    print(item['price'])


form = FormData()

for item in data:
    result = form.update_form(house_price=item['price'], house_address=item['address'], house_link=item['link'])
    if result is None:
        form.go_back()
        new_result = form.update_form(house_price=item['price'], house_address=item['address'], house_link=item['link'])
    else:
        continue

