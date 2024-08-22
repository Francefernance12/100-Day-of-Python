from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.write(f'SCORE: {self.score}', align="left", font=FONT)

    def increment_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
