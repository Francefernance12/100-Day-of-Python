import requests
from twilio.rest import Client
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# weather api data
OWM_ENDPOINT = getenv("WEATHER_API_URL")
API_KEY = "WEATHER API KEY HERE"
latitude = 00.0000
longitude = 00.0000
weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
    "cnt": 1
}
# twilio data
account_sid = "TWILIO SID HERE"  # placeholder
auth_token = "AUTHENTICATION TOKEN"  # placeholder

# response
weather_response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

for intervals in weather_data['list']:
    id_code = intervals['weather'][0]["id"]
    if int(id_code) < 700:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
             body="It's raining. You should take an umbrella",
             from_='+sender phone number',
             to='+recipient phone number'
            )

        print(message.status)
    else:
        print(id_code)
        print("You do not need an umbrella")
