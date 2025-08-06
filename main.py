# 35 API Authenticate

import requests
import datetime as dt


api_key = "0983b94d454a0bfa8a982b1f3b1bceae"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 49.414169,
    "lon": 14.658740,
    "cnt": 4,
    "appid": api_key,
}


response = requests.get(OWM_endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()


print(weather_data)


print(dt.datetime.fromtimestamp(1754449200))

