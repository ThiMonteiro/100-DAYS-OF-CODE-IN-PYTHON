import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "YOUR ACCOUNT SID" #SID DA SUA CONTA
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "YOUR LATITUDE", # SUA LATITUDE
    "lon": "YOUR LONGITUDE", # SUA LONGITUDE
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️", # Vai chover hoje. Lembre-se de trazer um ☔️
        from_="YOUR TWILIO VIRTUAL NUMBER", # SEU NÚMERO VIRTUAL TWILIO
        to="YOUR TWILIO VERIFIED REAL NUMBER" # SEU NÚMERO REAL VERIFICADO TWILIO
    )
    print(message.status)
