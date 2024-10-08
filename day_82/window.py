from tkinter import *
import json as js
import os

MORSE_CODE_ALPHABET = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


class MorseCodeConverter:

    def __init__(self):
        self.window = Tk()
        self.window.title("Morse Code Converter")
        self.window.minsize(width=400, height=300)
        self.window.geometry("450x500")

        # Label
        label = Label(self.window, text="Morse Code Converter", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Text box & button to convert
        input_label = Label(self.window, text="Input your text in english", font=("Arial", 16))
        input_label.grid(row=1, column=1, columnspan=2, pady=5)
        self.text_to_convert = Text(self.window, width=35, height=5, font=("Arial", 16), wrap='word')
        self.text_to_convert.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
        convert_button = Button(self.window, text="Convert", command=self.convert_text)
        convert_button.grid(row=3, column=1, columnspan=2, pady=5)

        # output (read only)
        output_label = Label(self.window, text="Output", font=("Arial", 16))
        output_label.grid(row=4, column=1, columnspan=2, pady=5)
        self.converted_output = Text(self.window, width=35, height=5, font=("Arial", 16), wrap='word')
        self.converted_output.grid(row=5, column=1, columnspan=2, padx=10, pady=5)
        self.converted_output.config(state=DISABLED)

        # Load existing json history
        self.history = None
        self.load_history()

        # Exit
        self.window.mainloop()

    # convert text to morse code then add text & morse code to json history
    def convert_text(self):
        # make the output write text
        self.converted_output.config(state=NORMAL)
        # Clear the previous output
        self.converted_output.delete('1.0', END)

        # Gets the text from the input
        get_input = self.text_to_convert.get('1.0', END).strip().upper()

        # converting process
        morse_code = [MORSE_CODE_ALPHABET[char] for char in get_input if char in MORSE_CODE_ALPHABET]
        output = ''.join(morse_code)

        # insert the morse code to output
        self.converted_output.insert(END, output)
        # turn the output state back to disabled state
        self.converted_output.config(state=DISABLED)

        # Update and save history to json
        self.update_history(get_input, output)

    # load existing json history(also creates a new one if it doesn't exist)
    def load_history(self):
        """Load history from a JSON file, or create a new history file if it doesn't exist."""
        if os.path.exists("morse_code_history.json"):
            with open("morse_code_history.json", 'r') as file:
                self.history = js.load(file)
        else:
            self.history = []

    # updates the json history
    def update_history(self, input_text, morse_code):
        new_entry = {
            "input_text": input_text,
            "morse_code": morse_code
        }
        self.history.append(new_entry)

        # Write the updated history to the file
        with open("morse_code_history.json", 'w') as file:
            js.dump(self.history, file, indent=4)
