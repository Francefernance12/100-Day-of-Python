from menu import Menu, MenuItem
from Main import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_menu = Menu()

is_on = True

while is_on:
    menu = coffee_menu.get_items()
    choice = input(f"WHAT WOULD YOU LIKE TO DRINK? {menu}\n").lower()

    # secret command
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        coffee = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)




