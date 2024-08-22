import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

input_is_typed = False
while not input_is_typed:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        input_is_typed = True
    except KeyError:
        print("Sorry, that is not in the dictionary")

