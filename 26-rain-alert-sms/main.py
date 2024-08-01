import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
generated_number = os.environ.get("NUMBER")

# Rohtok city is rainy
weather_params = {
    "lat": 28.895515,
    "lon": 76.606613,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Alert condition
will_rain = False
for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔.",
            from=generated_number,
            to="Your verified number"
    )
print(message.status)