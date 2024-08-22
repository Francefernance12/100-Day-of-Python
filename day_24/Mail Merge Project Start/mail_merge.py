
PLACEHOLDER = "[name]"

# sample letter
with open("Output/ReadyToSend/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()


# replacing the placeholder with the names
with open("Input/Letters/starting_letter.txt") as letters:
    letter_contents = letters.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)


