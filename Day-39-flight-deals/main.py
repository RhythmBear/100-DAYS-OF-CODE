# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager

data_manager = DataManager()
list_of_cities = data_manager.get_city_list()
print(list_of_cities)

resident_city = "LON"

today = dt.datetime.now().date()
till_date = today + dt.timedelta(days=180)
till_date = till_date.strftime("%d/%m/%Y")
print(till_date)


for city in list_of_cities:
    flight_search = FlightSearch()
    code = flight_search.get_destination_codes(city_name=city)

    data_manager.fill_iata_row(iata_value=code, city_name=city)

    flight_result = flight_search.check_flight(country_from=resident_city, city_to=code,
                                               from_time=today, to_time=till_date)
    flight_status = flight_result[0]
    flight_data = flight_result[1]

    if flight_status:
        price = flight_result[1].price

        price_check = data_manager.check_price(flight_price=price, city_name=city)

        if price_check:
            alert_message = f"Low price Alert! Only ${price} to " \
                            f"fly from {flight_data.departure_city_name}-{flight_data.airport_departure_iata_name}" \
                            f" to {flight_data.arrival_city}-{flight_data.arrival_airport_iata}, " \
                            f"from {flight_data.departure_date}" \
                            f" to {flight_data.return_date}"

            notif = NotificationManager()
            notif.send_text(message=alert_message)
            


# Flight requirements direct flights, leaves anytime between tomorrow and in 6 months, round trips that return between 7
# and 28 days in lenght currency of the price should be in GBP

