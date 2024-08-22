from BlackJackArt import logo, game_end
from random import randint
import sys


def calculate_score(cards):
    score = sum(cards)
    return score


# game over
def game_over():
    retry = input("Do you want to retry? Type 'y' or 'n': ").lower()
    if retry == "y":
        blackjack()
    else:
        print("Thanks for playing!")
        print(game_end)
        sys.exit()


# adds new card
def hit():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = cards[randint(0, len(cards) - 1)]

    return new_card


# chooses winner
def winners(player_score, computer_score, player_cards, computer_cards):
    print(f"Player score is, {player_score} and cards, {player_cards}")
    print(f"Computer score is, {computer_score} and cards, {computer_cards}")
    if player_score > computer_score:
        print("Player wins!")
        game_over()
    elif player_score < computer_score:
        print("Computer wins!")
        game_over()         # special rule for blackjack
    elif player_score == 21 and computer_score == 21:
        blackjack_draw = input("WOW! Two BlackJack! Do you want to push? Type 'y' or 'n': ")
        if blackjack_draw == "y":
            print("Push!")
            push(player_score, computer_score, player_cards, computer_cards)
        else:
            print("it's a draw!")
            game_over()
    else:
        print("It's a draw!")
        game_over()


def push(player_score, computer_score, player_cards, computer_cards):
    print("You and the computer have decided pushed.")
    # player_score
    new_player_card = hit()
    player_cards.append(new_player_card)
    new_player_score = calculate_score(player_cards)
    player_score += new_player_score
    print(f"Your new score is: {player_score} and player cards: {player_cards}")

    # new computer score
    new_computer_card = hit()
    computer_cards.append(new_computer_card)
    new_computer_score = calculate_score(computer_cards)
    computer_score += new_computer_score
    print(f"Computer new score is: {computer_score}. And computer card: {computer_cards}")

    # decides winner again
    if player_score == computer_score:
        retry = input("You both somehow looped back to the same score! Want to keep trying? type 'y' or 'n': ").lower()
        if retry == "y":
            push(player_score, computer_score, player_cards, computer_cards)
        elif retry == "n":
            game_over()
    else:
        input("push enter to see winner")
        winners(player_score, computer_score, player_cards, computer_cards)


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]   # cards: ace, 2-10, joker, queen, king
    # start
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        print(logo)
        # player
        player_cards = [cards[randint(0, len(cards) - 1)], cards[randint(0, len(cards) - 1)]]
        player_score = calculate_score(player_cards)

        if player_cards == 11 and player_cards == 10:
            player_score = 21
            print(f"Computer got a blackjack!")

        print(f"Your cards: {player_cards}. your current score {player_score}")

        # computer
        computer_cards = [cards[randint(0, len(cards) - 1)]]
        computer_score = sum(computer_cards)
        print(f"Computer's cards: {computer_cards}")

        bust = False
        while not bust:
            hit_pass = input("type 'hit' for another card or 'pass': ").lower()
            if hit_pass == "hit":      # "hit", will add another card to player list
                new_card = hit()
                player_cards.append(new_card)
                player_score = calculate_score(player_cards)

                print(f"Your cards: {player_cards}. your score {player_score}")
                if player_score > 21:
                    print(f"Busted! You went over 21! Your score: {player_score}. Computer Won!")
                    game_over()
                elif player_score > 21 and 11 in player_cards:
                    player_cards.remove(11)
                    player_cards.append(1)
                    player_score = calculate_score(player_cards)

                    print(f" Ace saved you! Player's current score: {player_score}")
            elif hit_pass == "pass":    # pass
                bust = True
        # after the player is done drawing cards, it will add the computer cards
        # computer score can't be less than 17
        while computer_score < 17:
            if computer_score < 17:
                new_computer_card = hit()
                computer_cards.append(new_computer_card)
                computer_score = calculate_score(computer_cards)
                if computer_score > 21:
                    print(f"Busted! Computer Lost! Computer score: {computer_score}. cards: {computer_cards}.")
                    print(f"Player won! Player score: {player_score}. cards: {player_cards}")
                    game_over()
                elif computer_score > 21 and 11 in computer_cards:
                    computer_cards.remove(11)
                    computer_cards.append(1)
                    computer_score = calculate_score(computer_cards)
                elif computer_cards == 11 and computer_cards == 10:
                    computer_score = 21
                    print(f"Computer has blackJack!")

            else:
                break

        winners(player_score, computer_score, player_cards, computer_cards)
    # player chooses pass
    else:
        print("Goodbye!")
        game_over()


blackjack()
