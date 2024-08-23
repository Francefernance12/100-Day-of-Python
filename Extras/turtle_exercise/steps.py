from turtle import Turtle, Screen

# screen
screen = Screen()
screen.setup(width=700, height=500, startx=0, starty=0)

# the turtle
turters = Turtle()
turters.shape("turtle")
turters.color("chocolate4")

# position

# movements
steps = 15
for _ in range(steps):
    turters.pendown()
    turters.forward(10)
    turters.penup()
    turters.forward(10)
    steps -= 1


# exit
screen.exitonclick()

