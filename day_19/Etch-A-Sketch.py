from turtle import Turtle, Screen

# screen
screen = Screen()
screen.setup(width=700, height=450)
screen.listen()

# the turtle object/stats
turters = Turtle()
turters.shape("turtle")
turters.speed(6)


# controls
def move_forward():
    turters.forward(10)


def move_backward():
    turters.backward(10)


def turn_left():
    turters.left(10)


def turn_right():
    turters.right(10)


def clear_screen():
    turters.clear()


def back_home():
    turters.penup()
    turters.home()
    turters.pendown()


# key controls
screen.onkeypress(fun=move_forward, key="Up")
screen.onkeypress(fun=turn_left, key="Left")
screen.onkeypress(fun=turn_right, key="Right")
screen.onkeypress(fun=move_backward, key="Down")
screen.onkeypress(fun=clear_screen, key="c")
screen.onkeypress(fun=back_home, key="h")

# exit
Screen().exitonclick()
