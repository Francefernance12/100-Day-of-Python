import pandas
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_TOP_TEXT = ("Ariel", 40, "italic")
FONT_BOTTOM_TEXT = ("Ariel", 60, "bold")

##########
#  DATA  #
##########
# French/English Words
try:
    data = pandas.read_csv("data/remaining_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')
    random_row = {}


###############
#  Functions  #
###############
# first command to run
def next_card():
    global random_row
    random_row = choice(data_dict)
    french_word = random_row["French"]
    canvas.itemconfig(flash_card_image, image=flash_card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")


# button functions
def is_known():
    global random_row, data_dict
    data_dict = [row for row in data_dict if row != random_row]  # Remove the current row

    # Save the remaining words to a CSV file
    known_words = pandas.DataFrame(data_dict)
    known_words.to_csv("./data/remaining_words.csv", index=False)

    english_side()


def english_side():
    canvas.itemconfig(flash_card_image, image=flash_card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_row["English"], fill="white")
    canvas.after(3000, next_card)


##########
#   UI   #
##########
# Windows
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=500)

# images
flash_card_front = PhotoImage(file="images/card_front.png")
flash_card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_image = canvas.create_image(400, 263, image=flash_card_front)
card_title = canvas.create_text(400, 150, text="", font=FONT_TOP_TEXT)
card_word = canvas.create_text(400, 263, text="", font=FONT_BOTTOM_TEXT)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
check_mark = Button(image=right, bg=BACKGROUND_COLOR, command=is_known)
check_mark.grid(row=1, column=1)
x_mark = Button(image=wrong, bg=BACKGROUND_COLOR, command=english_side)
x_mark.grid(row=1, column=0)

next_card()

# loop
window.mainloop()
