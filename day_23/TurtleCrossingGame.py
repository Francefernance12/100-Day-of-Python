import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

# screen
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=600, height=600)
screen.tracer(0)

# turtle
turters = Player()

# scoreboard
scoreboard = Scoreboard()

# cars
driving_cars = CarManager()

# controls
screen.listen()
screen.onkeypress(fun=turters.move_forward, key="Up")


# turtle crossing game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    driving_cars.move_car()
    for car in driving_cars.cars:
        # if turters makes it to goal
        if turters.ycor() > 280:
            turters.reset_position()
            scoreboard.increment_score()
            driving_cars.speed_up_car()
        # if car has collision with left wall, it will respawn to another location
        if car.xcor() < -300:
            car.goto(randint(300, 1000), randint(-240, 250))
        # turtle collision with car
        if turters.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
