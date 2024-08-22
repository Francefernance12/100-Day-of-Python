from turtle import Turtle

MOVEMENT_SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)  # 100 in height, 20 in width
        self.color("white")
        self.penup()
        self.goto(position)
        self.showturtle()

    def move_up(self):
        up = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), up)

    def move_down(self):
        down = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), down)
