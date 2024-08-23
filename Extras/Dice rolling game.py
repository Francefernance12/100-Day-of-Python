import random


def roll_dice():
    return random.randint(1, 6)


def loop():
    player_score = 0
    target_score = 20
    while player_score < target_score:
        start_rolling = input("press enter to roll the dice \n")

        if start_rolling == "":
            result = roll_dice()
            input(f'Your dice number is {result}.\n  Press Enter to roll again\n')
            player_score += result
            print(f'Your score is {player_score} \n')
        else:
            print("")


print(loop())
