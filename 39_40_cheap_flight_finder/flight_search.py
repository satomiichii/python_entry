import os
import requests
from dotenv import load_dotenv
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, destination):
        self.endpoint = 'https://tequila-api.kiwi.com/v2/search'
        self.from_city = 'NYC'
        self.to_city = destination
        self.from_date = ''
        self.to_date = ''
        self.get_date()
        self.result_list = []
        load_dotenv()

    def get_date(self):
        tomorrow = (dt.datetime.today() + dt.timedelta(days=1)).strftime(f'%d/%m/%Y')
        six_months = (dt.datetime.today() + dt.timedelta(days=180)).strftime(f'%d/%m/%Y')
        self.from_date = tomorrow
        self.to_date = six_months

    def fetch_flight_data(self):
        headers = {
            'apikey': os.environ['KIWI_API_KEY']
        }
        for city in self.to_city:
            params = {
                'fly_from': self.from_city,
                'fly_to': city,
                'date_from': self.from_date,
                'date_to': self.to_date,
                'nights_in_dst_from': 7,
                'nights_in_dst_to': 28,
                'flight_type': 'round',
                'max_stopovers': 0,
                'curr': 'USD'
            }
            response = requests.get(url=self.endpoint, params=params, headers=headers)
            response.raise_for_status()
            self.result_list.append(response.json())
        return self.result_list


