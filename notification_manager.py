import os
twilio_number = os.environ.get("twilio_number")
my_number = os.environ.get("my_number")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twi_num = twilio_number
        self.my_num = my_number
        self.sid = TWILIO_ACCOUNT_SID
        self.token = TWILIO_AUTH_TOKEN

    def notify(self, flight):
        send_message = f"Low price alert! Only ${flight.price} to fly from {flight.departure_city}-{flight.departure_iata_code} to {flight.arrival_city}-{flight.arrival_iata_code}, from {flight.departure_date} to {flight.arrival_date}."

        client = Client(self.sid, self.token)
        message = client.messages \
            .create(
            body=send_message,
            from_=self.twi_num,
            to=self.my_num
        )