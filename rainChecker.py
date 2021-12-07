# rainChecker.py
#
# Python Bootcamp Day 35 - Rain Checker
#
# Usage:
#   Using Twilio and OpenWeatherMap, send a text if rain is expected in next 11
#   hours. Can be automated on an online server like PythonAnywhere to send daily.
#
# Marceia Egler December 7, 2021
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LON")
WEATHER_API = os.getenv("WEATHER_API")
OWM_END = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_API,
    "exclude": "current,minutely,daily,alerts",
}

response = requests.get(OWM_END, params=weather_params)
response.raise_for_status()
data = response.json()
# Get next 11 hours weather data
weather_slice = data["hourly"][:12]
will_rain = False

for weather_data in weather_slice:
    condition_code = int(weather_data["weather"][0]["id"])

    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an ☂️",
        from_="+18506088282",
        to="+14076171799",
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Looks like no rain today.",
        from_="+18506088282",
        to="+14076171799",
    )
    print(message.status)
