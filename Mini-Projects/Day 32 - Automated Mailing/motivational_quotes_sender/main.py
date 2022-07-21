"""
This file will send motivational quotes through e-mail.
"""

import json
from smtplib import SMTP
from datetime import datetime
from calendar import day_name
import pandas as pd  # type: ignore[import]


def main() -> int:
    """
    This function will run the app.
    """
    # Mailing
    daily_spam()

    # Sending mail only if today is a monday ("0"):
    # send_mail_in_weekday(0)
    return 0


def send_mail_in_weekday(weekday: int, /) -> None:
    """
    Sends mail (calls "daily_spam()") if today is a given "weekday".
    "0" means monday, ..., "6" is sunday.
    """
    now = datetime.now()
    if now.weekday() == weekday:
        daily_spam()
    else:
        print(f"Today is {day_name[datetime.now().weekday()]}.")
        print(f"Messages are configured to be sent on {day_name[weekday]}s")


def daily_spam() -> None:
    """
    Sends randomly chosen quotes to everyone in ./data/mail_list.txt.
    """

    # Getting list of e-mails for us to "spam".
    with open("./data/mail_list.txt", encoding="utf-8") as file:
        emails: list[str] = file.read().strip().split("\n")

    # Getting user and password to access some e-mail account to send e-mails from.
    with open("./data/hidden.json", encoding="utf-8") as file:
        hidden_data: dict = json.load(file)

    # Opening CSV with quotes to send.
    quotes_data = pd.read_csv("./data/quotes/quotes.csv")

    subject: str = "Your daily motivational quote."
    complete_message: str = "Subject: {0}\r\n\r\n{1}"

    # Establishing a connection.
    with SMTP(hidden_data["smtp"]) as connection:
        connection.starttls()
        # Logging into an account in the file "./data/hidden.json"
        connection.login(user=hidden_data["e-mail"], password=hidden_data["password"])
        for email in emails:
            # Choosing random quote.
            quote: str = choose_quote(quotes_data, email)
            print(email)
            # Sending mail.
            connection.sendmail(
                msg=complete_message.format(subject, quote),
                from_addr=hidden_data["e-mail"],
                to_addrs=email,
            )

    # Saving back quotes.csv as its contents were updated in "choose_quote(...)" calls.
    quotes_data.to_csv("./data/quotes/quotes.csv", index=False)


def choose_quote(quotes_dataframe: pd.DataFrame, to_addr: str) -> str:
    """
    Receives a dataframe and an e-mail as input in string format.
    Returns a random quote in the dataframe that hasn't been already sent to that e-mail.
    Once all quotes have been sent to that e-mail, it will remove the e-mail from the dataframe
    and from quotes.csv, effectivelly "starting over".
    """

    quote: str | None = None
    # Iterating over all rows of the dataframe searching for a quote to send.
    # "sample(frac=1)" returns a copy of the dataframe with shuffled the rows but keeping
    # the correct index.
    for idx, row in quotes_dataframe.sample(frac=1).iterrows():
        # If it isn't an instance of a string, it's NaN (empty cell).
        if not isinstance(row["SentTo"], str):
            # Add email to that cell in the original dataframe.
            # It's the first email in that cell, so we can assign it directly.
            quotes_dataframe.at[idx, "SentTo"] = to_addr
            # Save quote.
            quote = row["Quotes"]
            # Breaking out of the loop because we already found our quote.
            break
        # Checking if this e-mail has already been added
        if to_addr not in row["SentTo"].split(","):
            # Add email to that cell in the original dataframe.
            # It isn't the first e-mail in that cell, so we're adding a ",".
            quotes_dataframe.at[idx, "SentTo"] += f",{to_addr}"
            # Save quote.
            quote = row["Quotes"]
            # Breaking out of the loop because we already found our quote.
            break

    # This situation should only happen if all quotes have already been sent to
    # the given e-mail.
    if quote is None:
        # Iterating through all rows.
        for idx, row in quotes_dataframe.iterrows():
            # Removing e-mail from all rows.
            emails = quotes_dataframe.at[idx, "SentTo"].split(",")
            emails.remove(to_addr)
            quotes_dataframe.at[idx, "SentTo"] = ",".join(emails)
            # If the cell ends up empty, turning "" into NaN.
            if quotes_dataframe.at[idx, "SentTo"] == "":
                quotes_dataframe.at[idx, "SentTo"] = pd.NA

        # Calling itself to do its job once again.
        quote = choose_quote(quotes_dataframe, to_addr)
    return quote


if __name__ == "__main__":
    raise SystemExit(main())
