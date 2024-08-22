import random

# Rock Paper Scissors
choices = ["rock", "paper", "scissors"]
choice_index = len(choices) - 1  # count the number of choices
computer_choice = random.randint(0, choice_index)  # computer picks a random number from 0 to the number of choices
player_choice = input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")  # User's choice

# what did the player choose
if player_choice == str(0):
    player_choice = choices[0]
    print("""player chose Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif player_choice == str(1):
    player_choice = choices[1]
    print(""" player chose Paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif player_choice == str(2):
    player_choice = choices[2]
    print("""player chose Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Invalid choice!")


# what did the computer choose
if computer_choice == 0:
    computer_choice = choices[0]
    print("""player chose Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice == 1:
    computer_choice = choices[1]
    print(""" player chose Paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer_choice == 2:
    computer_choice = choices[2]
    print("""player chose Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# win conditions
if player_choice == computer_choice:
    print("It's a tie!")
elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("Computer wins!")
