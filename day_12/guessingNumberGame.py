import random
from guessNumArt import winner, loser


# This will grab the random target number
def random_number():
    return random.randint(1, 100)


def guessing_number_game():
    target_number = random_number()  # random target number
    guess_count = 0  # increments until the limit

    print("guess the number! Hint! its a number between 1-100")
    # Choosing difficulty/setting guess limits
    guess_limit = 0
    choosing_difficulty = False
    while not choosing_difficulty:
        choose_difficulty = input("Choose a difficulty to choose \"easy\" or \"hard\" ").lower()
        if choose_difficulty == "easy":
            guess_limit = 10
            choosing_difficulty = True
        elif choose_difficulty == "hard":
            guess_limit = 5
            choosing_difficulty = True

    # incrementing the guessing count
    out_of_guesses = False
    while guess_count != guess_limit:
        guessing_number = int(input("guess the number: "))
        guess_count += 1
        print(f"your guess attempts {guess_count} out of {guess_limit}")
        # attempts
        if guessing_number == target_number:
            print(f"congrats! you win! The answer is {target_number}")
            print(winner)
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
        print(loser)


guessing_number_game()
