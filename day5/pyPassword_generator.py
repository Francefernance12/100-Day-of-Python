# pypassword generator
import random

# characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# inputs from user
select_letters = int(input("How many letters would you like in your password?\n"))
select_symbols = int(input(f"How many symbols would you like in your password?\n"))
select_numbers = int(input(f"How many numbers would you like in your password?\n"))

# empty password
password = str("")

# select random characters
for letter in range(0, select_letters):
    password += random.choice(letters)

for symbol in range(0, select_symbols):
    password += random.choice(symbols)

for number in range(0, select_numbers):
    password += random.choice(numbers)

password = list(password)  # Convert into list
random.shuffle(password)  # Shuffles the list to shuffle the password elements
new_password = "".join(password)  # Creates a new password to put the old password contents inside it

print(f"Your password is {new_password}")
