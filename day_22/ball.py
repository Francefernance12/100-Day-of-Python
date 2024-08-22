from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # simply moves the ball as long as the while loop is active.
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bounces ball off the top and bottom wall
    def bounce_off_wall(self):
        self.y_move *= -1

    # makes ball bounce off the opposite direction of the paddle
    def bounce_off_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # changes ball direction after it goes out of bounds
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_off_paddle()
