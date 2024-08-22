from Caesar_art import logo

# duplicate the alphabet to avoid out of range error
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# caesar cipher. This will shift each letter in the message by the shift amount.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":  # decryption or shift backward or left.
        shift_amount *= -1   # e.g 3 * -1 = -3
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)  # finds each letter from start_text inside the alphabet
            new_position = position + shift_amount  # shifts the letter to right
            end_text += alphabet[new_position]  # adds the new shifted letters
        else:
            end_text += char

    print(f"Here's the {cipher_direction}ed result: {end_text}")


# caesar cipher art
print(logo)

# This loop will run until the user types 'no'
in_game = True
while in_game:
    # inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # in case, there is a large shift amount that goes over the limit of the alphabet list

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # lets user restart the game
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == "no":
        in_game = False
        print("Goodbye!")
