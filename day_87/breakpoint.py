from turtle import Turtle


# breakpoint is the scoreboard
class BreakPoint(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.break_points = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(550, 200)
        self.write(self.break_points, align="center", font=("courier", 80, "normal"))

    def scored(self):
        self.break_points += 1

    def game_finished(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 80, "normal"))

