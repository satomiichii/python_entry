# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

data = DataManager()
destination_data = data.fetch_data()
destination = [to['iataCode'] for to in destination_data]

flight_search = FlightSearch(destination)
flight_data = flight_search.fetch_flight_data()
