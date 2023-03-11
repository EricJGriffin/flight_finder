import os
import requests
token = os.environ.get("token")
sheety_url = os.environ.get("sheety_url")
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = sheety_url
        self.token = token
        self.sheety_headers = {
            "Authorization": token
        }
    def get_cities_sheet(self):

        r = requests.get(url=self.url, headers=self.sheety_headers)
        return r.json()

    def set_code(self, city_dict):
        row = city_dict["id"]
        put_url = f"{self.url}/{row}"
        parameters = {
            "price": {
                "iataCode": city_dict["iataCode"]
            }
        }
        r = requests.put(url=put_url, json=parameters, headers=self.sheety_headers)
        r.raise_for_status()

