from tkinter import *
from random import choice
from time import time


class SpeedTyper:

    def __init__(self, paragraphs):
        self.window = Tk()
        self.window.title("Speed Typing Test")
        self.window.minsize(width=450, height=400)
        self.window.geometry("700x600")  # Increased size for better layout

        # Initialize timer variables
        self.start_time = None
        self.timer_running = False
        self.time_limit = 60  # seconds
        self.paragraphs = paragraphs
        self.selected_paragraph = choice(self.paragraphs)

        # Title
        label_title = Label(self.window, text="Speed Typing Test", font=("Arial", 20, "bold"))
        label_title.pack(pady=(20, 10))

        text_subtitle = Label(
            self.window,
            text="How fast are your fingers? Do the one-minute typing test to find out!",
            font=("Arial", 12)
        )
        text_subtitle.pack(pady=(0, 20))

        # Display text
        self.text_widget = Text(self.window, wrap="word", width=70, height=10, font=("Arial", 12))
        self.text_widget.pack(pady=10)
        self.text_widget.insert(END, self.selected_paragraph)
        self.text_widget.config(state=DISABLED, bg="#F0F0F0")  # Light grey background for readability

        # Entry box for typing
        self.entry_box = Entry(self.window, width=60, font=("Arial", 12))
        self.entry_box.pack(pady=10)
        self.entry_box.config(state=DISABLED)  # Disable initially
        self.entry_box.bind("<Return>", self.stop_timer_event)  # Allow stopping with Enter key

        # Timer label
        self.timer_label = Label(self.window, text="Press Start to Begin", font=("Arial", 14))
        self.timer_label.pack(pady=5)

        # Buttons Frame
        buttons_frame = Frame(self.window)
        buttons_frame.pack(pady=10)

        # Start button
        self.start_button = Button(
            buttons_frame,
            text="Start",
            command=self.start_timer,
            font=("Arial", 14),
            width=10,
            bg="#4CAF50",
            fg="white"
        )
        self.start_button.grid(row=0, column=0, padx=10)

        # Stop button
        self.stop_button = Button(
            buttons_frame,
            text="Stop",
            command=self.stop_timer,
            font=("Arial", 14),
            width=10,
            bg="#f44336",
            fg="white",
            state=DISABLED
        )
        self.stop_button.grid(row=0, column=1, padx=10)

        # Reset button
        self.reset_button = Button(
            buttons_frame,
            text="Reset",
            command=self.reset_test,
            font=("Arial", 14),
            width=10,
            bg="#008CBA",
            fg="white"
        )
        self.reset_button.grid(row=0, column=2, padx=10)

        # Exit button
        self.exit_button = Button(
            self.window,
            text="Exit",
            command=self.window.quit,
            font=("Arial", 14),
            width=10,
            bg="#555555",
            fg="white"
        )
        self.exit_button.pack(pady=10)

        # Result label
        self.result_label = Label(self.window, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

        # Focus management: Initially, focus is on the Start button
        self.start_button.focus_set()

        # Start the Tkinter main loop
        self.window.mainloop()

    def start_timer(self):
        if not self.timer_running:
            self.start_time = time()
            self.timer_running = True
            self.update_timer()
            self.start_button.config(state=DISABLED)
            self.stop_button.config(state=NORMAL)
            self.reset_button.config(state=DISABLED)
            self.entry_box.config(state=NORMAL)
            self.entry_box.delete(0, END)
            self.result_label.config(text="")
            self.timer_label.config(text=f"{self.time_limit} seconds remaining")
            self.entry_box.focus_set()

    def update_timer(self):
        if self.timer_running:
            current_time = time()
            elapsed_time = current_time - self.start_time
            time_remaining = self.time_limit - int(elapsed_time)

            if time_remaining > 0:
                self.timer_label.config(text=f"{time_remaining} seconds remaining")
                self.window.after(1000, self.update_timer)
            else:
                self.timer_label.config(text="Time's up!")
                self.stop_timer()

    def stop_timer_event(self, event):
        # Handles stopping the timer when Enter key is pressed.
        self.stop_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.stop_button.config(state=DISABLED)
            self.start_button.config(state=DISABLED)  # Prevent restarting without reset
            self.reset_button.config(state=NORMAL)
            self.entry_box.config(state=DISABLED)

            # Calculate Words Per Minute (WPM)
            typed_text = self.entry_box.get().strip()
            word_count = len(typed_text.split())
            elapsed_time = time() - self.start_time
            time_minutes = elapsed_time / 60
            wpm = word_count / time_minutes if time_minutes > 0 else 0

            # Calculate Accuracy
            accuracy = self.calculate_accuracy(typed_text)

            # Display Results
            self.result_label.config(text=f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%")

    def calculate_accuracy(self, typed_text):
        """Calculates the accuracy of the typed text compared to the sample text."""
        sample_words = self.selected_paragraph.split()
        typed_words = typed_text.split()
        correct = 0

        for i in range(min(len(sample_words), len(typed_words))):
            # Compare words ignoring punctuation and case
            sample_word = sample_words[i].strip("-_").lower()
            typed_word = typed_words[i].strip("-_").lower()
            if sample_word == typed_word:
                correct += 1

        total = len(sample_words)
        accuracy = (correct / total) * 100 if total > 0 else 0
        return accuracy

    def reset_test(self):
        # Resets the test to allow the user to retake it.
        self.timer_running = False
        self.start_time = None
        self.timer_label.config(text="Press Start to Begin")
        self.start_button.config(state=NORMAL)
        self.stop_button.config(state=DISABLED)
        self.reset_button.config(state=NORMAL)
        self.entry_box.config(state=NORMAL)
        self.entry_box.delete(0, END)
        self.result_label.config(text="")

        # Select a new paragraph
        self.selected_paragraph = choice(self.paragraphs)
        self.text_widget.config(state=NORMAL)
        self.text_widget.delete("1.0", END)
        self.text_widget.insert(END, self.selected_paragraph)
        self.text_widget.config(state=DISABLED)

        # Set focus back to the Start button
        self.start_button.focus_set()