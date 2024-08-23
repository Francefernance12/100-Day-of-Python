from turtle import Turtle, Screen
from random import choice

# screen
screen = Screen()
screen.setup(width=700, height=800, startx=0, starty=0)

# the turtle object
turters = Turtle()
turters.shape("turtle")

# colors
colors = ["lime", "orange", "yellow", "dark red", "light blue", "medium violet red", "medium violet red"]


# drawing shapes
def draw_shape():
    shapes_left = 8
    sides = 3
    while shapes_left > 0:
        for _ in range(sides):
            angles = 360 / sides
            turters.forward(100)
            turters.right(angles)

        sides += 1
        shapes_left -= 1
        turters.color(choice(colors))


draw_shape()

# exit
screen.exitonclick()
