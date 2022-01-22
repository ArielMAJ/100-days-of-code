from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep
import os


def clear():
    """Clears the console screen. Right-Click the
file and select "Modify Run Configuration"
and enable "emulate terminal in output console".
"""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    turned_on = True
    while turned_on:
        clear()
        choice = input(f"What would you like? [{menu.get_items()}] ")

        if choice == 'report':
            coffee_maker.report()
            money_machine.report()
            sleep(1.5)
        elif choice == "off":
            turned_on = False
        else:
            drink = menu.find_drink(choice)
            if drink != None and coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                sleep(2.5)
            sleep(1.5)


if __name__ == "__main__":
    main()
