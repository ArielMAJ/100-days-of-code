import pandas as pd

nato_data_frame = pd.read_csv("./nato_phonetic_alphabet.csv")
# print(nato_data_frame)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for index, row in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Write a word: ").upper()
print([nato_dict[letter] for letter in user_input])
