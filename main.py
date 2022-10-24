# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for row in sheet_data:
    cheapest_flight_data = flight_search.get_price(row['iataCode'])
    print(f"{row['city']} : IDR {cheapest_flight_data[0]} Departure Date: {cheapest_flight_data[1]}")
    format_data = FlightData()
    flight = format_data.format_flight_data(cheapest_flight_data)

    if flight[0] < row["lowestPrice"]:

        price = flight[0]
        departure_date = flight[1]
        departure_city_name = "Jakarta"
        departure_IATA = "CGK"
        arrival_city_name = row["city"]
        arrival_IATA = row["iataCode"]
        send_notification = NotificationManager()

        send_notification.send_message(price, departure_date, departure_city_name, departure_IATA, arrival_city_name,
                                       arrival_IATA)
