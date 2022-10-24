"""
This file implements the weather class.
"""

from datetime import datetime
import requests
from hidden_data_handler import HiddenData


class Weather:
    """
    Weather class.
    """

    def __init__(self):
        self._hidden = HiddenData()
        self.request_data()

    @property
    def data(self):
        """
        This property returns the full weather data.
        """
        return self._data

    def request_data(self):
        """
        This function will load the current weather data into this class.
        """
        url = "https://api.openweathermap.org/data/2.8/onecall"

        params = {
            "lat": self._hidden.lat,
            "lon": self._hidden.lon,
            "appid": self._hidden.api_key,
            "exclude": "current,minutely,daily",
        }

        resp = requests.get(url, params=params)
        resp.raise_for_status()

        self._data = resp.json()

    def should_bring_an_umbrella(self) -> bool:
        """
        This function will look into the next 12 hours and return true if you should
        take an umbrella or false if you won't need it.
        """
        for hour in self.data["hourly"][:12]:
            for weather in hour["weather"]:
                if weather["id"] < 700:
                    print(datetime.fromtimestamp(hour["dt"]))
                    return True

        return False


def main() -> int:
    """
    Main function. This is to help easily visualize and test the class created in this file.
    """
    weather = Weather()
    print(weather.should_bring_an_umbrella())

    # print(weather.data["hourly"][0])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
