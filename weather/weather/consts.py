import json

# get config from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

WEATHER_API_KEY: str = config[
    "WEATHER_API_KEY"
]  # Replace with your OpenWeatherMap API key
BASE_URL: str = "http://api.openweathermap.org/data/2.5/weather"
