import turtle as t
from turtle import Turtle, Screen
from random import choice, randint

# screen
screen = Screen()
screen.setup(width=700, height=800, startx=0, starty=0)
t.colormode(255)

# the turtle object/stats
turters = Turtle()
turters.shape("turtle")
turters.speed(10)
turters.pensize(10)


# colors
def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


# random walk
directions = [0, 90, 180, 270]
for _ in range(200):
    turters.setheading(choice(directions))
    turters.color(random_colors())
    turters.forward(50)

# exit
screen.exitonclick()
