from calcArt import logo


# operations
def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


# main calculator app
def calculator():
    print("Welcome to the calculator!")
    print(logo)

    operations = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
    }

    num1 = int(input("Enter the first number: "))

    # reveals all operation symbols for user to choose
    for operation in operations:
        print(operation)

    # while loop for User to continue calculating
    while True:
        operator = input("Enter the operator: ")
        num2 = int(input("Enter the next number: "))
        calculation_function = operations[operator]  # selects the operator from dictionary
        answer = calculation_function(num1, num2)   # calculates the answer

        print(f"{num1} {operator} {num2} = {answer}")

        # User has three choices to continue calculating
        retry = input(f"type 'y' to continue calculation with {answer} or 'n' to quit or 't' to reset calculator: ")
        if retry == "n":
            print("Goodbye!")  # leaves
            break
        elif retry == "y":
            num1 = answer  # keeps the answer as the first number
        elif retry == "t":
            calculator()   # resets calculator
        else:
            print("Invalid input. Please try again.")


calculator()
