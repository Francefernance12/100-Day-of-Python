from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
AMOUNT_OF_CARS = 25


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_increment = MOVE_INCREMENT
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.add_cars()

    def add_cars(self):
        for _ in range(0, AMOUNT_OF_CARS):
            self.create_cars()

    def create_cars(self):
        car = Turtle()
        car.shape("square")
        car.setheading(180)
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(choice(COLORS))
        car.goto(randint(300, 1000), randint(-240, 250))
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.starting_move_distance)

    def speed_up_car(self):
        self.starting_move_distance += self.move_increment

