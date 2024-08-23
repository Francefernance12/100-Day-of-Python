import random


def random_number():
    return random.randint(1, 10)


print("guess the number! Hint! its a number between 1-10")


def attempt():
    target_number = random_number()
    guess_count = 0
    guess_limit = 5
    out_of_guesses = False

    while True:
        guessing_number = int(input("guess the number: "))
        guess_count += 1
        # attempts
        if guessing_number == target_number:
            print("congrats! you win!")
            break
        elif guess_count >= guess_limit:
            out_of_guesses = True
            break
        else:
            # indicators
            if guessing_number < target_number:
                print("Try a higher number")
            else:
                print("Try a lower number")
    if out_of_guesses:
        print(f"You're out of guesses! The number was {target_number}. You lose!")


attempt()
