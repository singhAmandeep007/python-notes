from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

from . import consts

import requests


# https://openweathermap.org/current
class WeatherCondition(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int


class WeatherResponse(BaseModel):
    coord: Dict[str, float] = Field(description="Geographical coordinates")
    weather: List[WeatherCondition] = Field(description="Weather conditions")
    base: str
    main: Optional[Main] = None
    visibility: int
    wind: Dict[str, float] = Field(description="Wind details")
    rain: Optional[Dict[str, float]] = None
    clouds: Dict[str, int] = Field(description="Cloud cover information")
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int


def get_weather(data: Dict[str, float]) -> WeatherResponse:
    """
    Retrieves weather data.

    Args:
        data (Dict[str, float]): Query parameters.

    Returns:
        WeatherResponse: The weather data for the specified location.
    """

    data.update({"appid": consts.WEATHER_API_KEY, "units": "metric"})

    data["lon"] = data.pop("lng")

    response: requests.Response = requests.get(consts.BASE_URL, params=data)
    if response.status_code == 200:
        try:
            data: WeatherResponse = WeatherResponse.model_validate(response.json())
            return data.model_dump()
            # return response.json()
        except Exception as e:
            raise Exception(f"Failed to parse weather data: {e}")
    else:
        raise Exception(
            f"Failed to retrieve weather data. Status code: {response.status_code}"
        )
