# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = DataManager()
destination_data = data.fetch_data()

search = FlightSearch()
flight_msg = FlightData
sms = NotificationManager()

for destination in destination_data:
    flight = search.fetch_flight_data(destination['iataCode'])
    if flight and flight['price'] < destination['lowestPrice']:
        print(flight)
        message = flight_msg.create_message(flight)
        sms.send_message(message)
    else:
        print('No deal for today')
