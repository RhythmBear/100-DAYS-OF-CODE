
class FlightData:
    # This class is responsible for structuring the flight data_manager.
    def __init__(self, price, departure_city, airport_from, city_to, airport_to, out_date, in_date):
        self.price = price
        self.departure_city_name = departure_city
        self.airport_departure_iata_name = airport_from
        self.arrival_city = city_to
        self.arrival_airport_iata = airport_to
        self.departure_date = out_date
        self.return_date = in_date
