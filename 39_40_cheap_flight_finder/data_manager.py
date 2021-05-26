import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = 'https://api.sheety.co/fb1328f8715a7846e6fb218f820926eb/flightDeals/prices'

    def fetch_data(self):
        response = requests.get(self.endpoint).json()
        return response['prices']
