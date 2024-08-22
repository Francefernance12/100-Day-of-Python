from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# labels
# miles
miles = Label(text="Miles")
miles.grid(column=2, row=0)
# Kilometer
kilometer = Label(text="Km")
kilometer.grid(column=2, row=1)
# is equal to
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
# result
result = Label(text=0)
result.grid(column=1, row=1)


# convert miles to kilometers
def miles_to_km():
    miles_numbers = float(miles_input.get())
    kilometers = miles_numbers * 1.60934
    result.config(text=f"{kilometers}")


# entry
miles_input = Entry(width=9)
miles_input.grid(column=1, row=0)

# Button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
