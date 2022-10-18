import requests
import datetime as dt
from data_manager import DataManager

TEQUILA_ID = "rhythmbearflightproject"
TEQUILA_API_KEY = "x7YRkkQ6ojzm3AxsXmgFXExQTxqb7Vpa"
TEQUILA_NEW_API_KEY = "Cy3tpsonhfjZIECAFjiFuEMjj_lMe0lY"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
iata_codes = {'Paris': 'PAR', 'Berlin': 'BER', 'Tokyo': 'TYO', 'Sydney': 'SYD', 'Istanbul': 'IST',
              'Kuala Lumpur': 'KUL', 'New York': 'NYC', 'San Francisco': 'SFO', 'Cape Town': 'CPT'}

# for state in list:
#     location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
#     header = {"apikey": TEQUILA_API_KEY}
#     query = {
#         "term": state,
#         "location_type": "city"
#     }
#
#     response = requests.get(url=location_endpoint, params=query, headers=header)
#
#     result = response.json()
#     code = result['locations'][0]['code']
#
#     iata_codes[state] = code
#
# print(iata_codes)

today = dt.datetime.now().date()
date_10 = today + dt.timedelta(days=10)
date_10 = date_10.strftime("%d/%m/%Y")
print(date_10)


headers = {
    "apikey": TEQUILA_NEW_API_KEY
}

query = {
    "fly_from": "LON",
    "fly_to": "PAR",
    "date_from": today.strftime("%d/%m/%Y"),
    "date_to": date_10,
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP",

}
responses = {}

for (city, code) in iata_codes.items():
    query = {
        "fly_from": "LON",
        "fly_to": code,
        "date_from": today.strftime("%d/%m/%Y"),
        "date_to": date_10,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "GBP"

    }
    search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
    response = requests.get(url=search_endpoint, params=query, headers=headers)
    flight_json = response.json()

    responses[city] = flight_json

    try:
        data = response.json()['data'][0]

    except IndexError or KeyError:
        print(f"No information found for a flight to {city}")

    else:
        flight_price = data['price']

        print(f"London -> {city} will cost: ${flight_price}")

        data_man = DataManager()
        data_man.check_price(flight_price, city)


