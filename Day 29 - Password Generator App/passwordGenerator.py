from random import choice, randint, shuffle


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '_',
            '.', ',', '<', '>', ':', ';', '?', '/', '\\','^', '~', '[',']','{','}', '\'', '\"']

def generate_password():
    nr_letters = randint(4, 11)
    nr_numbers = randint(4, 15-nr_letters)
    nr_symbols = 20 - (nr_numbers + nr_letters)

    password = [choice(letters) for _ in range(nr_letters)] + \
    [choice(numbers) for _ in range(nr_numbers)] + \
    [choice(symbols) for _ in range(nr_symbols)]

    shuffle(password)
    return ''.join(password)