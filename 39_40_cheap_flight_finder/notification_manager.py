import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, flight_data):
        message = self.client.messages \
            .create(
            body=flight_data,
            from_=os.environ['SENDER_NUMBER'],
            to=os.environ['TO_NUMBER']
        )

        print(message.status)
