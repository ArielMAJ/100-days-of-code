"""
This is day's 33 main project. This project will check if it is night time in your current position
(latitude and longitude). If it is, it will compare your position to the ISS's and if the ISS is
above you it will notify you to look at the sky to see it.
"""

from datetime import datetime
import time
import json
import requests

with open("Resources/latlon.json", encoding="utf-8") as file:
    HIDDEN_DATA = json.load(file)


def iss_current_latlon() -> tuple[float, float]:
    """
    This function returns the current latitude and longitude of the ISS.
    """
    url = "http://api.open-notify.org/iss-now.json"

    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    return iss_latitude, iss_longitude


def is_night_time() -> bool:
    """
    This function will take your latitude and logintude and return whether it
    currently is nighttime there.
    """
    url = "http://api.sunrise-sunset.org/json"

    params = {
        "lat": HIDDEN_DATA["MY_LAT"],
        "lon": HIDDEN_DATA["MY_LON"],
        "formatted": 0,
    }

    resp = requests.get(url, params=params)
    resp.raise_for_status()

    data = resp.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    return sunset <= time_now.hour or time_now.hour <= sunrise


def iss_is_above_me() -> bool:
    """
    This function will take your latitude and logintude and return whether the ISS
    currently is about you.
    """
    iss_latitude, iss_longitude = iss_current_latlon()
    my_lat, my_lon = float(HIDDEN_DATA["MY_LAT"]), float(HIDDEN_DATA["MY_LON"])
    return (my_lat - 5 < iss_latitude < my_lat + 5) and (
        my_lon - 5 < iss_longitude < my_lon + 5
    )


def notify_me() -> None:
    """
    This was expected to be sending e-mails but, as this lesson was about APIs, I preferred to just
    print.
    """
    print("Look up at the sky, the ISS is over you!")


def main() -> int:
    """
    Main function.
    """
    while True:
        if not is_night_time():
            # print("Not night time.")
            # break
            time.sleep(1800)
            continue

        if iss_is_above_me():
            notify_me()
            time.sleep(540)
        # else:
        # print("ISS is not above you.")
        # break

        time.sleep(60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
