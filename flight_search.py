import os
flight_search_url = os.environ.get("flight_search_url")
location_path = "locations/query"
search_path = "v2/search"
apikey = os.environ.get("apikey")
import requests
import datetime as dt
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = flight_search_url
        self.loc_path = location_path
        self.search_path = search_path
        self.apikey = apikey
        self.headers = {
            "accept": "application/json",
            "apikey": apikey,
        }

    def get_city_code(self, city_dict):
        parameters = {
            "term": city_dict["city"],
            "location_types": "city",
        }

        search_url = self.url + self.loc_path
        r = requests.get(url=search_url, params=parameters, headers=self.headers)
        return r.json()["locations"][0]["code"]

    def get_cheapest_flight(self, city_dict):
        today = dt.datetime.today()
        tomorrow = (today + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (today + dt.timedelta(days=182)).strftime("%d/%m/%Y")
        parameters = {
            "fly_from": "BDL",
            "fly_to": city_dict["iataCode"],
            "date_from": tomorrow,
            "date_to": six_months,
            "price_to": city_dict["lowestPrice"],
            "curr": "USD",
        }
        flight_url = self.url + self.search_path
        r = requests.get(url=flight_url, params=parameters, headers=self.headers)
        return r.json()