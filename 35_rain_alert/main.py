import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

params = {
    'lat': '38.627003',
    'lon': '-90.199402',
    'exclude': 'current,minutely,daily',
    'appid': os.environ['API_KEY']
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)

is_rain = False

for i in range(12):
    main_weather = data['hourly'][i]['weather'][0]['id']
    if main_weather < 700:
        print(f"It will rain in {i} hours")
        is_rain = True
        break


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

if is_rain:
    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring umbrella ☂️",
                         from_=os.environ['SENDER_NUMBER'],
                         to=os.environ['TO_NUMBER']
                     )

    print(message.status)

