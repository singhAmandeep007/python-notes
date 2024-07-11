import argparse

import logging

from weather.weather_api import get_weather


logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="get_weather.log",
    format="%(asctime)s %(levelname)s: %(message)s",
    filemode="w",
    level=logging.DEBUG,
)


def get_current_weather_info_by_lat_lng(lat: float = None, lng: float = None):
    """
    Args:
        lat (float): Latitude of the location.
        lng (float): Longitude of the location.
    Raises:
        ValueError: If both lat and lng are missing or if lat or lng are out of bounds.
        KeyError: If the required data is missing.
        Exception: If there is an error getting the weather data.
    Returns:
        dict: The weather information for the specified location.

    """
    if lat is None or lng is None:
        raise ValueError("Latitude and longitude must not be None")

    if not -90 <= lat <= 90:
        raise ValueError("Latitude must be between -90 and 90 degrees")

    if not -180 <= lng <= 180:
        raise ValueError("Longitude must be between -180 and 180 degrees")

    try:
        weather_data = get_weather({"lat": lat, "lng": lng})

        try:
            description = weather_data["weather"][0]["description"]
        except (KeyError, IndexError):
            description = None
        try:
            temperature = weather_data["main"]["temp"]
        except KeyError:
            temperature = None

        if temperature is None or description is None:
            raise KeyError("Required data is missing")

        return {"description": description, "temperature": temperature}
    except KeyError as e:
        print(f"Error getting current weather info: {e}")
        # Re-raise the KeyError
        raise
    except Exception as e:
        print(f"Error getting current weather info: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Get weather information for a location"
    )

    parser.add_argument(
        "--lat",
        type=float,
        default=40.7128,
        help="Latitude of the location (default: 40.7128 - New York City)",
    )
    parser.add_argument(
        "--lng",
        type=float,
        default=-74.0060,
        help="Longitude of the location (default: -74.0060 - New York City)",
    )

    args = parser.parse_args()

    try:
        info = get_current_weather_info_by_lat_lng(args.lat, args.lng)
        description = info.get("description")
        temperature = info.get("temperature")

        print(
            f"Weather for coordinates ({args.lat}, {args.lng}): \n Description: {description} \n Temperature: {temperature} °C"
        )

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
