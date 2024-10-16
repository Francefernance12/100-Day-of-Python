from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green"]
AMOUNT_OF_BRICKS = 112
BRICK_START_X = -450
BRICK_START_Y = 250
BRICK_WIDTH = 70
BRICK_HEIGHT = 30
BRICKS_PER_ROW = 14


class BrickManager:
    def __init__(self):
        self.bricks = []
        self.add_bricks()

    def add_bricks(self):
        x_pos = BRICK_START_X
        y_pos = BRICK_START_Y
        for i in range(0, AMOUNT_OF_BRICKS):
            self.create_bricks((x_pos, y_pos))
            x_pos += BRICK_WIDTH
            # Move to the next row after filling one row
            if (i + 1) % BRICKS_PER_ROW == 0:
                x_pos = BRICK_START_X  # Reset x position
                y_pos -= BRICK_HEIGHT  # Move to the next row

    def create_bricks(self, position):
        brick = Turtle()
        brick.shape("square")
        brick.setheading(180)
        brick.turtlesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.color(choice(COLORS))
        brick.goto(position)
        self.bricks.append(brick)

