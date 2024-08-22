from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score_board import Scoreboard

# screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # To control the auto screen update. animation is off.
screen.mode("standard")  # for X and Y coordinates

# ball object
ball = Ball()

# left and right paddle objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# player's scoreboard object
scoreboard = Scoreboard()

screen.listen()
# player 1 control keys
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

# player 2 control keys
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

# pong game
game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()  # creates animation
    ball.move_ball()
    # collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()
    # Right paddle collision
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_scored()
        scoreboard.update_scoreboard()
    # left paddle collision
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_scored()
        scoreboard.update_scoreboard()
    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_off_paddle()
    # speed up the ball


# exit
screen.exitonclick()
