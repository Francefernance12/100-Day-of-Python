from turtle import Turtle

MOVEMENT_SPEED = 40


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)  # 100 in height, 20 in width
        self.color("white")
        self.penup()
        self.goto(position)
        self.showturtle()

    def move_right(self):
        right = self.xcor() + MOVEMENT_SPEED
        self.goto(right, self.ycor())

    def move_left(self):
        left = self.xcor() - MOVEMENT_SPEED
        self.goto(left, self.ycor())
