"""
This file will send birthday letters to people having birthday in the day this is run.
"""

import json
from smtplib import SMTP
from datetime import datetime
from glob import glob
import random
import pandas as pd  # type: ignore[import]


def main() -> int:
    """
    This function will run the app.
    """
    check_birthdays()
    return 0


def check_birthdays() -> None:
    """
    Sends an e-mail to people having birthdays today.
    """
    # Getting user and password to access some e-mail account to send e-mails from.
    with open("./hidden.json", encoding="utf-8") as file:
        hidden_data = json.load(file)

    # Turning CSV with people's data into pandas DataFrame.
    birthday_list = pd.read_csv("./birthdays.csv")
    # Getting paths to birthday letter templates.
    letter_paths = glob("./letter_templates/*.txt")

    # Getting today's date.
    now = datetime.now()
    todays_month_and_day = (now.month, now.day)

    # Iterating through every person in the csv/dataframe
    for _, row in birthday_list.iterrows():
        # If today is this persons birthday.
        if (row["month"], row["day"]) == todays_month_and_day:
            # Choose a random letter template to send.
            letter_path = random.choice(letter_paths)
            # Get letter as string and fill in the person's name.
            with open(letter_path, encoding="utf-8") as file:
                letter = file.read().replace("[NAME]", row["name"])
            # Send them the letter.
            sendmail(row["email"], letter, hidden_data)


def sendmail(to_addr: str, letter: str, hidden_data: dict) -> None:
    """
    E-mails a happy birthday letter to "to_addr".
    """
    complete_message: str = f"Subject: Happy Birthday!\r\n\r\n{letter}"

    # Establishing a connection.
    with SMTP(hidden_data["smtp"]) as connection:
        connection.starttls()
        # Logging into an account in the file "./hidden.json"
        connection.login(user=hidden_data["e-mail"], password=hidden_data["password"])
        print(to_addr)
        # Sending mail.
        connection.sendmail(
            msg=complete_message,
            from_addr=hidden_data["e-mail"],
            to_addrs=to_addr,
        )


if __name__ == "__main__":
    raise SystemExit(main())
