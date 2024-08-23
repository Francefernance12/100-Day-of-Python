import turtle as t
from turtle import Turtle, Screen
from random import choice, randint

# screen
screen = Screen()
screen.setup(width=700, height=800, startx=0, starty=0)
t.colormode(255)


def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


# the turtle object/stats
turters = Turtle()
turters.shape("turtle")
turters.speed("fastest")
turters.pensize(1)

for _ in range(100):
    turters.circle(90)
    turters.left(5)
    turters.color(random_colors())

# exit
screen.exitonclick()
