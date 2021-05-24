import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.environ['NUTRITION_API_KEY']
APP_ID = os.environ['APP_ID']
NUT_END_POINT = ' https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_END_POINT = 'https://api.sheety.co/fb1328f8715a7846e6fb218f820926eb/workoutTracker/workouts'
SHEETY_AUTH = os.environ['SHEETY_AUTH']

query_input = input('Tell me which exercise you did:').lower()

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

param = {
    'query': query_input
}

response = requests.post(url=NUT_END_POINT, json=param, headers=headers)
response.raise_for_status()
data = response.json()
print(data)

today = datetime.now()
date_str = today.strftime(f'%m/%d/%Y')
time_str = today.strftime("%H:%M:%S")

sheety_header = {
    'Authorization': f'Bearer {SHEETY_AUTH}',
    "Content-Type": "application/json"
}

for index in data['exercises']:
    sheety_params = {
        'workout': {
            'date': date_str,
            'time': time_str,
            'exercise': index['name'].title(),
            'duration': index['duration_min'],
            'calories': index['nf_calories'],
        }
    }

    response = requests.post(url=SHEETY_END_POINT, json=sheety_params, headers=sheety_header)
    response.raise_for_status()
    print(response)
