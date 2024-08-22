import random
from Hangman_words import word_list
from Hangman_art import logo
from Hangman_art import stages

# random words and length of the randomized word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# number of lives.
lives = 6

print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# entire game loop
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # Check if user is wrong. Lose a life.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    # hangman art

    print(stages[lives])
