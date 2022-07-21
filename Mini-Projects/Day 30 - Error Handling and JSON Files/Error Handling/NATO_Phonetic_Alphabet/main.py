import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error:
        print(f"{error} is not a valid character. Please use only letters.\n")
    else:
        break

print('', output_list, sep="\n", end="\n\n")
