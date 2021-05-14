import requests
import datetime as dt
import smtplib

MY_LAT = 40.730610
MY_LONG = -73.935242
MY_EMAIL = 'my_email.com'
MY_PASSWORD = 'my_password'

# ----- Fetch ISS location--------#

iss_data = requests.get(url='http://api.open-notify.org/iss-now.json')
iss_data.raise_for_status()
location = iss_data.json()['iss_position']
iss_location = (float(location['latitude']), float(location['longitude']))

print(iss_location)

# ----- Fetch Current Location's Sunrise & Sunset Time -----#
param = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=param)
response.raise_for_status()
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

print(sunrise, sunset)

sunrise_time = int(sunrise.split('T')[1].split(':')[0])
sunset_time = int(sunset.split('T')[1].split(':')[0])

# ----- Fetch Current Hour -----#
now = dt.datetime.utcnow()
current_hour = now.hour

print(current_hour)


# ----- Check is it's night time and ISS is close to where you are -----#

def check_location_time():
    if MY_LAT - 5 < iss_location[0] > MY_LAT + 5 and MY_LONG - 5 < iss_location[1] > MY_LONG + 5:
        if current_hour >= sunset_time or current_hour <= sunrise_time:
            return True
    return False


# ----- Send email to myself to notify the ISS is above you ------#

if check_location_time():
    print('Look the sky')
    # with smtplib.SMTP('smtp.google.com') as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL,
    #                         to_addrs=MY_EMAIL,
    #                         msg='Subject: Look at the sky!\n\nISS is right above your location')
