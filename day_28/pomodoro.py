from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # 25
SHORT_BREAK_MIN = 5  # 5
LONG_BREAK_MIN = 20  # 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkMark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in list(range(1, 7, 2)):
        title.config(text="Start Working", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        count_down(work_sec)
    elif reps in range(2, 6, 2):
        marks = ""
        reps_cut = floor(reps/2)
        for _ in range(reps_cut):
            marks += "✓"
        checkMark.config(text=marks, fg=GREEN)
        title.config(text="Take a Short Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        title.config(text="Take a Long Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)
        count_down(long_break_sec)
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Pomodoro Break")
window.config(padx=100, pady=50, bg=YELLOW)

# tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)
checkMark = Label(fg=GREEN)
checkMark.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
