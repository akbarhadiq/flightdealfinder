import datetime

import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv("secrets.env")

TEQUILA_ENDPOINT_GET = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_ENDPOINT_SEARCH = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
tequila_header = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        params = {
            "term": city_name
        }
        response = requests.get(url=TEQUILA_ENDPOINT_GET, headers=tequila_header, params=params)
        code = response.json()["locations"][0]["code"]
        return code

    def get_price(self, IATA_name):
        params = {
            "fly_from": "CGK",
            "fly_to": IATA_name,
            "date_from": dt.datetime.now().strftime("%d/%m/%Y"),
            "date_to": (dt.datetime.now() + datetime.timedelta(days=(30 * 6))).strftime("%d/%m/%Y"),
            "curr": "IDR"
        }
        response = requests.get(url=TEQUILA_ENDPOINT_SEARCH, headers=tequila_header, params=params)
        lowest_price = 10000000000000000000
        departure_date = None
        price_list = response.json()["data"]

        for x in range(len(price_list)):
            if price_list[x]["price"] < lowest_price:
                lowest_price = price_list[x]["price"]
                departure_date = price_list[x]["route"][0]["local_departure"]

        return [lowest_price, departure_date, ]


# new = FlightSearch()
# flight_data = new.get_price("TYO")

# print(flight_data[0]["route"])

# print(flight_data[0]["route"][0])

# lowest_price = 1000000000000000
# departure_date = None
#
# for x in range(len(flight_data)):
#     if flight_data[x]["price"] < lowest_price:
#         lowest_price = flight_data[x]["price"]
#         departure_date = flight_data[x]["route"][0]["local_departure"]
#
# print(lowest_price)
# print(departure_date)

# it WOROORKKSKS!