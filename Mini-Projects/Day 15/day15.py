import data
import os
from time import sleep


def clear():
    """Clears the console screen. Right-Click the
file and select "Modify Run Configuration"
and enable "emulate terminal in output console".
"""
    os.system('cls' if os.name == 'nt' else 'clear')


def enough_resources(coffee):
    """Checks if resources are enough for making this coffee. Returns True if there are, else False."""
    enough = True
    for ingredient, amount_needed in data.MENU[coffee]['ingredients'].items():
        if data.resources[ingredient] < amount_needed:
            print(f"Sorry there is not enough {ingredient}")
            enough = False

    return enough


def insert_coins():
    for coin in data.COIN_TYPES:
        try:
            data.CURRENT_USER_CHANGE += int(input(f"How many {coin} are you inserting? "))*data.COIN_TYPES[coin]
        except:
            continue


def got_coins(coffee):
    """Checks if there are enough coins. Returns True if there are, else False."""
    insert_coins()
    while data.CURRENT_USER_CHANGE < data.MENU[coffee]['cost']:
        clear()
        print(f"Sorry ${data.CURRENT_USER_CHANGE}'s not enough money. Please insert ${data.MENU[coffee]['cost']}.")
        action = input(f"Press enter to insert more or 0 to cancel action.\n")
        if action == '0':
            data.CURRENT_USER_CHANGE = 0
            print("Money refunded.")
            sleep(2)
            return False
        else:
            insert_coins()
    data.MONEY_IN_THE_MACHINE += data.MENU[coffee]['cost']
    data.CURRENT_USER_CHANGE -= data.MENU[coffee]['cost']

    clear()
    if data.CURRENT_USER_CHANGE > 0:
        print(f"Here's your's ${data.CURRENT_USER_CHANGE} dollars change.\n")
        data.CURRENT_USER_CHANGE = 0.0
        sleep(2.5)
    return True


def serve_coffee(coffee):
    """Servers coffee."""
    for ingredient, amount_needed in data.MENU[coffee]['ingredients'].items():
        data.resources[ingredient] -= amount_needed
    print(f"Here's your {coffee}. Enjoy!")
    return


def report():
    """Prints to the screen the amount of resources left and money acquired."""
    for resource in data.resources:
        print(f'{resource.capitalize()}: {data.resources[resource]}{"ml" if resource!="coffee" else "g"}')
    print(f'Money: ${data.MONEY_IN_THE_MACHINE:.2f}')
    return


def main():
    while True:
        clear()
        action = input(f'What would you like? ({"/".join(data.MENU.keys())}): ')

        if action in data.MENU.keys():
            if enough_resources(action) and got_coins(action):
                serve_coffee(action)
                sleep(2)
            sleep(1)
        elif action == 'report':
            report()
            input("\nPress enter to continue. ")
            continue
        elif action == 'off':
            break
        else:
            print("\nInvalid option, try again.")
            sleep(1)



if __name__ == '__main__':
    main()

