## Setup

1. [Poetry](../README.md)

## How to run get_weather.py ?

1. cd into weather directory
2. Run `poetry run python get_weather.py --lat=44.34 --lng=10.99`
   1. Note: lat and lng defaults to New York if not provided.

## How to run tests ?

1. cd into weather directory
2. Run `poetry run pytest -vv -s` or `poetry run test`

## How to run formatter ?

1. cd into weather directory
2. Run `poetry run black .`

## Weather API

1. Call current Weather data Eg. https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
