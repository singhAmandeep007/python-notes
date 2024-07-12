import unittest
import pytest

from unittest.mock import patch
from weather.get_weather import get_current_weather_info_by_lat_lng

import logging

# By using the __name__ attribute as the name of the logger, it allows the logger to be uniquely identified based on the module it belongs to.
logger = logging.getLogger(__name__)


@pytest.fixture
def mock_weather_data():
    return {"weather": [{"description": "clear sky"}], "main": {"temp": 20.5}}


@pytest.fixture
def mock_get_weather(mock_weather_data):
    with patch(
        "weather.get_weather.get_weather", return_value=mock_weather_data
    ) as mock:
        yield mock


def test_get_current_weather_info_by_lat_lng_success(mock_get_weather):
    result = get_current_weather_info_by_lat_lng(40.7128, -74.0060)
    assert result == {"description": "clear sky", "temperature": 20.5}


def test_get_current_weather_info_by_lat_lng_none_values():
    with pytest.raises(ValueError, match="Latitude and longitude must not be None"):
        get_current_weather_info_by_lat_lng()


def test_get_current_weather_info_by_lat_lng_one_none_value():
    with pytest.raises(ValueError, match="Latitude and longitude must not be None"):
        get_current_weather_info_by_lat_lng(40.7128, None)


def test_get_current_weather_info_by_lat_lng_api_error(mock_get_weather, capfd):
    mock_get_weather.side_effect = Exception("API Error")
    result = get_current_weather_info_by_lat_lng(40.7128, -74.0060)
    assert result is None
    captured = capfd.readouterr()
    assert "Error getting current weather info: API Error" in captured.out


def test_get_current_weather_info_by_lat_lng_missing_data(mock_get_weather):
    incomplete_data = {"weather": [{}], "main": {}}
    mock_get_weather.return_value = incomplete_data
    with pytest.raises(KeyError):
        get_current_weather_info_by_lat_lng(40.7128, -74.0060)


@pytest.mark.parametrize(
    "lat,lng",
    [
        (90, 180),
        (-90, -180),
        (0, 0),
    ],
)
def test_get_current_weather_info_by_lat_lng_boundary_values(
    lat, lng, mock_get_weather
):
    result = get_current_weather_info_by_lat_lng(lat, lng)
    assert result == {"description": "clear sky", "temperature": 20.5}


if __name__ == "__main__":
    unittest.main()
