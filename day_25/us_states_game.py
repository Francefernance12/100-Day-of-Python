import turtle
import pandas

# Map screen
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. States Game")
screen.tracer(0)

# States Data
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# font
font = ('Arial', 8, 'normal')

# U.S Guessing Game
game_is_on = True
guessed_correctly = []
while game_is_on:
    # Inputs
    answer_states = (screen.textinput(title=f"{len(guessed_correctly)}/50 States correct", prompt="What's another "
                                                                                                  "state's "
                                                                                                  "name?").title()
                     .strip())
    print(answer_states)
    # secret 'Exit' command. Creates save file in csv
    if answer_states == "Exit":
        missing_states = [state for state in states if state not in guessed_correctly]
        saved_data = pandas.DataFrame(missing_states)
        saved_data.to_csv("states_to_learn.csv")
        game_is_on = False
    # if user guessed correctly
    if answer_states not in guessed_correctly:
        for state in states:
            if answer_states == state:
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                coordinates = data[data.state == state]
                x = int(coordinates.iloc[0]["x"])
                y = int(coordinates.iloc[0]["y"])
                print(x, y)
                t.goto(x, y)
                t.write(arg=f"{state}", font=font)
                screen.update()
                guessed_correctly.append(answer_states)
    # win condition
    if len(guessed_correctly) == 50:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 0)
        t.write(arg="You've guessed all states correctly! Game Over!", font=font)
        game_is_on = False

screen.exitonclick()
