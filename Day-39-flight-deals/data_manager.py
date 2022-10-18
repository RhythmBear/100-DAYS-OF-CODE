import requests
from flight_data import FlightData
from pprint import pprint


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self, url="https://api.sheety.co/6058f50226857081a997dc586d44aa18/copyOfFlightDeals/prices"):
        self.url = url
        self.country_list = []
        iata_codes = {}

        self.response = requests.get(url=self.url)

        self.sheet_data = self.response.json()
        # self.prices_list contains a dictionary of all the data_manager in the google sheet
        self.prices_list = self.sheet_data["prices"]

        # The iata test value is a string that is used to fill in the rows in the google sheet, used to test the code
        self.iata_test_value = ""

    def get_city_list(self):
        """Returns the List of Countries in the google sheets"""
        self.country_list = [item['city'] for item in self.prices_list]

        return self.country_list
        # pprint(sheet_data)
        # print(city_list)

    def fill_iata_row(self, iata_value, city_name):
        for dic in self.prices_list:
            if city_name == dic['city']:
                # Checks to see if the iata row in each data_manager piece is filled or empty
                if len(dic['iataCode']) >= 1:
                    body = {
                        'price': {
                            "iataCode": iata_value
                        }
                    }

                    response = requests.put(url=f"{self.url}/{dic['id']}", json=body)
                    print(response.text)

    def check_price(self, flight_price, city_name):
        for city in self.prices_list:
            if city_name == city['city']:
                min_price = city['lowestPrice']

                print(f"{min_price} vs {flight_price}")

                if min_price >= flight_price:
                    return True
                elif flight_price > min_price:
                    return False
