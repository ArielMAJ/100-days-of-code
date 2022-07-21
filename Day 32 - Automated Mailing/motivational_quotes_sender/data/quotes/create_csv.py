"""
File for a simple creation of a quotes CSV.
Expects that there are txt files in the same folder for processing.
It will overwrite older versions of quotes.csv.
"""

from glob import glob
import random
import pandas as pd  # type: ignore[import]

# Getting all txt paths.
paths = glob("./*.txt")

# Adding all quotes to a list, line per line (for every txt path).
quotes = []
for path in paths:
    with open(path, encoding="utf-8") as quotes_file:
        quotes.extend(quotes_file.readlines())

# Shuffling quotes.
random.seed(42)
random.shuffle(quotes)

# Creating dataframe
data = pd.DataFrame(quotes, columns=["Quotes"])
data["SentTo"] = pd.NA

# Testing adding to a cell.
# data.at[0, "SentTo"]="ariel.maj@hotmail.com"

# Looking at dataframe:
print(data.head())

# Saving to CSV:
data.to_csv("./quotes.csv", index=False)
data.to_csv("./backup_quotes.csv", index=False)

# Selecting a random quote:
# Won't be really "random" because of the seed selected above.
print(random.choice(quotes))
