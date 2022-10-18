import requests
from flight_data import FlightData

TEQUILA_ID = "rhythmbearflightproject"
TEQUILA_API_KEY = "x7YRkkQ6ojzm3AxsXmgFXExQTxqb7Vpa"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_NEW_API_KEY = "Cy3tpsonhfjZIECAFjiFuEMjj_lMe0lY"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.iata_dict = {}

    def get_destination_codes(self, city_name):
        """ Returns an iata_code for every city name passed into the
         function and also creates a (city_name: code pair) in the iata_dict and stores it in there"""

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_type": "city"}

        response = requests.get(url=location_endpoint, params=query, headers=headers)

        result = response.json()
        code = result["locations"][0]["code"]

        self.iata_dict[city_name] = code

        return code

    def check_flight(self, country_from: str, city_to, from_time, to_time):

        headers = {
            "apikey": TEQUILA_NEW_API_KEY
        }

        query = {
            "fly_from": country_from,
            "fly_to": city_to,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",

        }

        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        response = requests.get(url=search_endpoint, params=query, headers=headers)
        # print(response.text)

        try:
            flight_data = response.json()['data'][0]

        except IndexError or KeyError:
            print("No information found on that city")
            return False, "No information found"

        else:
            flight_price = flight_data['price']
            city_from = flight_data["route"][0]['cityFrom']
            airport_from = flight_data["route"][0]['flyFrom']
            city_to = flight_data["route"][0]['cityTo']
            airport_to = flight_data["route"][0]['flyTo']
            departure_date = flight_data["route"][0]["local_departure"].split("T")[0]
            return_date = flight_data["route"][1]["local_departure"].split("T")[0]

            new_flight_data = FlightData(price=flight_price, departure_city=city_from,
                                         airport_from=airport_from,
                                         city_to=city_to, airport_to=airport_to,
                                         out_date=departure_date, in_date=return_date)

            return True, new_flight_data



