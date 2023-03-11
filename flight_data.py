class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flight_dict):
        self.departure_iata_code = flight_dict["flyFrom"]
        self.arrival_iata_code = flight_dict["flyTo"]
        self.departure_city = flight_dict["cityFrom"]
        self.arrival_city = flight_dict["cityTo"]
        self.price = flight_dict["price"]
        self.departure_date = flight_dict["local_departure"]
        self.arrival_date = flight_dict["local_arrival"]
