#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
fs = FlightSearch()
dm = DataManager()
nm = NotificationManager()
cities_list = dm.get_cities_sheet()["prices"]

for city in cities_list:
    if not city["iataCode"]:
        code = fs.get_city_code(city)
        city["iataCode"] = code
        dm.set_code(city)
    #get cheapest flight for code for tomorrow to 6 months out
    flight_dict = fs.get_cheapest_flight(city)
    if flight_dict["_results"] > 0:
        for flight in flight_dict["data"]:
            structured_flight = FlightData(flight)
            nm.notify(structured_flight)


