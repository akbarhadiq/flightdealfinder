import os
from dotenv import load_dotenv
from pprint import pprint
import requests

# pretty print

load_dotenv("secrets.env")


# sheety_auth = os.getenv("sheety_token")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.sheety_auth = os.getenv("sheety_token")
        self.sheety_get_url_endpoint = "https://api.sheety.co/2b7440464c17d783b68e68faf726e0a3/flightDeals/prices"
        self.sheety_put_url_endpoint = "https://api.sheety.co/2b7440464c17d783b68e68faf726e0a3/flightDeals/prices/"
        self.sheety_headers = {
            "Authorization": self.sheety_auth
        }

    def get_destination_data(self):
        response = requests.get(url=self.sheety_get_url_endpoint, headers=self.sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{self.sheety_put_url_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
