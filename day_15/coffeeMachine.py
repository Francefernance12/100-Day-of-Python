import sys
from day_15.Data.coffeeData import MENU, resources


# report
def report(profit):
    print(f"WATER: {resources['water']}")
    print(f"MILK: {resources['milk']}")
    print(f"COFFEE: {resources['coffee']}")
    print(f"COST: ${profit}\n")


# refunds the user or change
def refund(user_amount, coffee_cost):
    return round(user_amount - coffee_cost, 2)


# checks if the user paid enough for the drink
def successful_transaction(user_amount, coffee_cost):
    if user_amount < coffee_cost:
        print(f"SORRY THAT'S NOT ENOUGH MONEY. MONEY REFUNDED: ${user_amount}\n")
        return False
    elif user_amount >= coffee_cost:
        return True


# checks if there are enough resources
def is_sufficient(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] >= resources[ingredient]:
            print(f"SORRY, NOT ENOUGH: {ingredient}\n")
            return True
    return False


# takes away all the resources used by the user. Depending on the coffee chosen.
def used_ingredients(coffee_ingredients):
    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]


# calculates all the coins together
def insert_coin(user_amount):
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25

    inserted_quarters = int(input("HOW MANY QUARTERS? "))
    inserted_dimes = int(input("HOW MANY DIMES? "))
    inserted_nickels = int(input("HOW MANY NICKELS? "))
    inserted_pennies = int(input("HOW MANY PENNIES? "))

    # penny
    total_penny = penny * inserted_pennies
    user_amount += total_penny
    # nickel
    total_nickel = nickel * inserted_nickels
    user_amount += total_nickel
    # dime
    total_dime = dime * inserted_dimes
    user_amount += total_dime
    # quarter
    total_quarter = quarter * inserted_quarters
    user_amount += total_quarter

    return round(user_amount, 2)


# main coffee maker program
def coffee_machine():
    # secret words for maintainers to turn off the system
    turn_off = "off"
    reports = "report"

    # coffee
    espresso = MENU['espresso']
    latte = MENU['latte']
    cappuccino = MENU['latte']

    # cost
    espresso_cost = espresso['cost']
    latte_cost = latte['cost']
    cappuccino_cost = cappuccino['cost']

    # overall profit for report
    profit = 0.00

    while True:
        print(f"☕ESPRESSO COSTS: ${espresso_cost}")
        print(f"☕LATTE COSTS: ${latte_cost}")
        print(f"☕CAPPUCCINO COSTS: ${cappuccino_cost}")
        choice = input("WHAT WOULD YOU LIKE TO DRINK? (ESPRESSO/LATTE/CAPPUCCINO)\n").lower()

        # secret commands
        if choice == turn_off:
            print("PROGRAM HAS TURNED OFF")
            sys.exit()
        elif choice == reports:
            print("HERE IS THE REPORT")
            report(profit)
            continue
        else:       # checks if the drink has enough resources
            coffee_ingredients = MENU[choice]['ingredients']
            insufficient = is_sufficient(coffee_ingredients)
            if insufficient:
                print("TRY ANOTHER DRINK\n")
                continue

        # User's coffee choice
        user_amount = 0.00
        if choice == 'espresso':
            print(f"INSERT YOUR COINS\n")
            user_amount = insert_coin(user_amount)
            acceptable_transaction = successful_transaction(user_amount, espresso_cost)
            if acceptable_transaction:      # refund
                refund_amount = refund(user_amount, espresso_cost)
            else:
                continue
            profit += user_amount
            profit -= refund_amount
            print(f"YOU INSERTED: ${user_amount}. YOUR REFUND IS: {refund_amount}.")
            print(f"HERE IS A ESPRESSO\n")
        elif choice == 'latte':
            print(f"INSERT YOUR COINS\n")
            user_amount = insert_coin(user_amount)
            acceptable_transaction = successful_transaction(user_amount, latte_cost)
            if acceptable_transaction:      # refund
                refund_amount = refund(user_amount, latte_cost)
            else:
                continue
            profit += user_amount
            profit -= refund_amount
            print(f"YOU INSERTED: ${user_amount}. YOUR REFUND IS: {refund_amount}.")
            print("HERE IS A LATTE\n")
        elif choice == 'cappuccino':
            print(f"INSERT YOUR COINS\n")
            user_amount = insert_coin(user_amount)
            acceptable_transaction = successful_transaction(user_amount, cappuccino_cost)
            if acceptable_transaction:      # refund
                refund_amount = refund(user_amount, cappuccino_cost)
            else:
                continue
            profit += user_amount
            profit -= refund_amount
            print(f"YOU INSERTED: ${user_amount}. YOUR REFUND IS: {refund_amount}.")
            print("HERE IS A CAPPUCCINO\n")
        else:
            print("ERROR, TYPE AGAIN\n")
        # remove resources based on how many resources was used
        used_ingredients(coffee_ingredients)


coffee_machine()
