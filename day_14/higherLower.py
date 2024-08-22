from random import choice
from higherLowerArt import logo, vs
from replit import clear
from gameData import data


# increment score
def increment_score(score):
    score += 1
    return score


# pick a random famous person from list
def random_person():
    # pick a random dictionary
    index = choice(range(len(data)))

    name = data[index]['name']
    followers = data[index]['follower_count']
    description = data[index]['description']
    country = data[index]['country']
    return name, followers, description, country


# the game
def higher_lower():
    score = 0
    wrong_answer = False
    while not wrong_answer:
        print(logo)
        print(f"Score: {score}")
        # opponent a
        name, followers, description, country = random_person()
        opponent_a = [name, followers, description, country]
        # a profile
        a_name = opponent_a[0]
        a_followers = opponent_a[1]
        a_description = opponent_a[2]
        a_country = opponent_a[3]

        # opponent b
        name, followers, description, country = random_person()
        opponent_b = [name, followers, description, country]
        # b profile
        b_name = opponent_b[0]
        b_followers = opponent_b[1]
        b_description = opponent_b[2]
        b_country = opponent_b[3]

        if opponent_a == opponent_b:
            continue

        # display
        print(f"Competitor A: {a_name}, {a_description}, {a_country}")
        print(vs)
        print(f"Competitor B: {b_name}, {b_description}, {b_country}")

        # choices
        player_choice = input("who has the most followers? Choose 'A' or 'B' ").lower()
        clear()
        if a_followers > b_followers and player_choice == "a":
            print("correct!")
            score = increment_score(score)
        elif b_followers > a_followers and player_choice == "b":
            print("correct!")
            score = increment_score(score)
        else:
            print("Sorry! Wrong Answer! GAME OVER!")
            print(f"Final Score: {score}")
            wrong_answer = True


higher_lower()
