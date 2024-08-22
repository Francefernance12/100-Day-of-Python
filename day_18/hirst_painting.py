import turtle as t
from turtle import Turtle, Screen
from random import choice

# screen
screen = Screen()
screen.setup(width=700, height=450)

# color mode
t.colormode(255)

# coordinates
y = -200
x = -300

# the turtle object/stats
turters = Turtle()
turters.shape("turtle")
turters.speed(6)
turters.penup()
turters.goto(x, y)

# Hirst colors
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60),
              (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

# hirst painting
rows = 7
while rows > 0:
    for _ in range(12):      # columns
        turters.dot(20, choice(color_list))
        turters.hideturtle()
        turters.forward(50)
        turters.showturtle()
    y += 50
    turters.goto(x, y)
    rows -= 1

# exit
Screen().exitonclick()
