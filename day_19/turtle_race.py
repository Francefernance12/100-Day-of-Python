from turtle import Turtle, Screen
from random import randint

# screen
screen = Screen()
screen.setup(width=500, height=400)


# the turtle object/instances
all_turtle = []
turtle_colors = ["green", "blue", "red", "yellow", "purple", "orange"]
y_position = 60
for turtle in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle])
    new_turtle.goto(x=-230, y=y_position)
    y_position -= 25
    all_turtle.append(new_turtle)

# the bet
user_bet = screen.textinput(title="Make a Bet Dude", prompt="Which turtle do you think will win? ('green', 'blue', "
                                                            "'red', 'yellow', 'purple', 'orange'").lower()

# The race
race_is_on = False
if user_bet:
    race_is_on = True

    while race_is_on:

        for racing_turtle in all_turtle:

            if racing_turtle.xcor() > 230:
                winner = racing_turtle.color()
                if winner[0] != user_bet:
                    print(f"The Winner is {winner[0]} Turtle! You Lost the Bet!")
                    race_is_on = False
                else:
                    print(f"The Winner is {winner[0]} Turtle! you guessed correctly!")
                    race_is_on = False
            random_distance = randint(0, 10)
            racing_turtle.forward(random_distance)


# exit
Screen().exitonclick()
