# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

import os
import requests
from datetime import datetime
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from pprint import pprint
from notification_manager import NotificationManager

data = DataManager()
destination_data = data.fetch_data()
destination = [to['iataCode'] for to in destination_data]
print(destination)

flight_search = FlightSearch(destination)
flight_data = flight_search.fetch_flight_data()
# print(flight_data[0])
