class FlightData:

    def format_flight_data(self, data):
        flight_price = data[0]
        date_split = data[1].split("T")
        departure_date = date_split[0]

        return [flight_price, departure_date]

