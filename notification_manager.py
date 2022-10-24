import smtplib
from dotenv import load_dotenv
import os

load_dotenv("secrets.env")

my_email = os.getenv("MY_EMAIL")
smtp = os.getenv("SMTP")
password = os.getenv("password")
port = os.getenv("port")


class NotificationManager:

    def send_message(self, price, departure_date, departure_city, departure_iata, arrival_city, arrival_iata):

        price_ = price
        departure_date_ = departure_date
        departure_city_ = departure_city
        departure_iata_ = departure_iata
        arrival_city_ = arrival_city
        arrival_iata_ = arrival_iata

        connection = smtplib.SMTP(smtp, 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="virtuesof@protonmail.com",
            msg=f"Subject:Flight Deal\n\n" \
                f"Only IDR {price_} to fly from {departure_city_}-{departure_iata_} to {arrival_city_}-{arrival_iata_} "
                f"at {departure_date_}"
        )
        connection.close()
