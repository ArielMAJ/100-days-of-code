"""
This file implements the "HiddenData" class.
"""

import json


class HiddenData:
    """
    A class to facilitate reading and using "hidden" data (as in data
    I don't want to upload/publish).
    """

    def __init__(self):
        self._api_key: str
        self._lat: str
        self._lon: str

        self.reset_class_params()

    @property
    def api_key(self) -> str:
        """
        This property returns the api key in the hidden json file.
        """
        return self._api_key

    # @api_key.setter
    # def api_key(self, api_key: str):
    #     self._api_key = api_key

    @property
    def lat(self) -> str:
        """
        This property returns the latitude in the hidden json file.
        """
        return self._lat

    @property
    def lon(self) -> str:
        """
        This property returns the longitude in the hidden json file.
        """
        return self._lon

    def reset_class_params(self):
        """
        This function will read the hidden json file and reset all parameters
        (or set then for the first time when initializing the class).
        """
        with open("Resources/hidden.json", encoding="utf-8") as file:
            hidden_data = json.load(file)

        self._api_key = hidden_data["api_key"]
        self._lat = hidden_data["MY_LAT"]
        self._lon = hidden_data["MY_LON"]


def main() -> int:
    """
    Main function. This is to help easily visualize and test the class created in this file.
    """
    hidden = HiddenData()
    print(
        hidden.api_key,
        hidden.lat,
        hidden.lon,
        sep="\n",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
