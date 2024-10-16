from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = choice([10, -10])
        self.y_move = -10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_off_top_wall(self):
        self.y_move *= -1

    def bounce_off_left_right_wall(self):
        self.x_move *= -1

    def bounce_off_brick(self):
        self.y_move *= -1

    def bounce_off_paddle(self, paddle):
        # Calculate the difference between the ball's x position and the paddle's x position
        x_diff = self.xcor() - paddle.xcor()
        self.x_move = max(min(x_diff * 0.3, 15), -15)  # limits
        self.y_move *= -1  # ball bounce
        self.move_speed *= 0.9  # Increase speed slightly on each paddle hit

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move = choice([10, -10])  # Start in a random X direction
