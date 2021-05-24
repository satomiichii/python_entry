import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()
USER_NAME='satomi'
graph_id = 'graph1'

habit_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': os.environ['PIXELA_TOKEN'],
    'username': USER_NAME,
    'agreeTermsOfService': "yes",
    "notMinor": "yes"
}

# response = requests.post(habit_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{habit_endpoint}/{USER_NAME}/graphs"


graph_config = {
    'id': graph_id,
    'name': 'Reading Graph',
    'unit': 'Minutes',
    'type': 'int',
    'color': 'ichou'
}

headers = {
    'X-USER-TOKEN': os.environ['PIXELA_TOKEN']
}

today = datetime.now()

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# response.raise_for_status()
# print(response.text)

create_pixel_endpoint = f"{habit_endpoint}/{USER_NAME}/graphs/{graph_id}"

new_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '45',
}

# response = requests.post(url=create_pixel_endpoint, headers=headers, json=new_params)
# response.raise_for_status()
# print(response.text)

update_pixel_endpoint = f'{habit_endpoint}/{USER_NAME}/graphs/{graph_id}/20210523'

update_params = {
    'quantity': '1100'
}

response = requests.put(url=update_pixel_endpoint, headers=headers, json=update_params)
response.raise_for_status()
print(response.text)