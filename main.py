# 35 API Authenticate

import requests
import datetime as dt


api_key = "0983b94d454a0bfa8a982b1f3b1bceae"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 17.246373,
    "lon": -10.672252,
    "cnt": 4,
    "appid": api_key,
}


response = requests.get(OWM_endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()


print(weather_data["list"][0]["weather"])


will_rain = False

for hour_data in weather_data["list"]:
    time = dt.datetime.fromtimestamp(hour_data["dt"])
    condition_code = int(hour_data["weather"][0]["id"])

    if condition_code < 700:
        will_rain = True
    print(f"{time.hour}:00", condition_code)

if will_rain is True:
    print("Bring the umbrella.")

