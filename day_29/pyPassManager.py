from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    complete_password = "".join(password_list)

    password_entry.insert(0, complete_password)
    copy(complete_password)


# ---------------------------- SEARCH FILE ------------------------------- #
def find_password():
    website_name = website_entry.get()
    try:
        with open("save_data.json") as sd:
            data = json.load(sd)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    else:
        if website_name in data:
            email_data = data[website_name]["email"]
            password_data = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email_data}\n Password: {password_data}")
        else:
            messagebox.showinfo(title="error", message=f"no details for {website_name} exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email_user_info = email_user_entry.get()
    password_info = password_entry.get()
    new_data = {
        website_name: {
            "email": email_user_info,
            "password": password_info
        }
    }
    if website_name == "" or email_user_info == "" or password_info == "":
        messagebox.showinfo(title="Empty Field", message="You left the Field Empty")
    else:
        try:
            with open("save_data.json", "r") as sd:
                # reading old data
                data = json.load(sd)
        except FileNotFoundError:
            with open("save_data.json", "w") as sd:
                json.dump(new_data, sd, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("save_data.json", "w") as sd:
                # saving updated data
                json.dump(data, sd, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Windows
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)


# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# label
website = Label(text="Website:")
website.grid(column=0, row=1)
email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# buttons
generate_password = Button(text="Generate Password", command=generate_random_password)
generate_password.grid(column=2, row=3, sticky=(E, W, N, S))
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky=(E, W, N, S))
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=(E, W, N, S))
add_button.config(width=36)

# entry
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky=(E, W, N, S))
website_entry.config(width=35)
website_entry.focus()
email_user_entry = Entry()
email_user_entry.grid(column=1, row=2, columnspan=2, sticky=(E, W, N, S))
email_user_entry.config(width=35)
email_user_entry.insert(0, "@example.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=(E, W, N, S))
password_entry.config(width=21)

window.mainloop()
