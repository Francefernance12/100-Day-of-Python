from turtle import Screen
from paddle import Paddle
from ball import Ball
from breakpoint import BreakPoint
from bricks import BrickManager
from time import sleep


def setup_screen():
    """Sets up the game screen."""
    screen = Screen()
    screen.setup(width=1400, height=650)
    screen.bgcolor("black")
    screen.title("Breakout")
    screen.tracer(0)  # Disable auto screen updates for smooth animation
    screen.mode("standard")  # Use standard X and Y coordinates
    return screen


def setup_controls(screen, paddle):
    """Binds the paddle movement keys."""
    screen.listen()
    screen.onkeypress(paddle.move_left, "a")
    screen.onkeypress(paddle.move_right, "d")


def handle_collisions(ball, paddle, bricks, scoreboard):
    """Handles all collisions in the game."""
    # Collision with top wall
    if ball.ycor() > 300:
        ball.bounce_off_top_wall()

    # Collision with left and right walls
    if ball.xcor() < -460 or ball.xcor() > 460:
        ball.bounce_off_left_right_wall()

    # Collision with paddle
    if ball.distance(paddle) < 35 and ball.ycor() > -320:
        ball.bounce_off_paddle(paddle)

    # Collision with floor
    if ball.ycor() < -370:
        ball.reset_position()

    # Collision with bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 30:
            ball.bounce_off_brick()
            brick.hideturtle()  # Remove the brick visually
            bricks.bricks.remove(brick)  # Remove the brick from the list
            scoreboard.scored()
            scoreboard.update_scoreboard()


def game_loop(screen, ball, paddle, bricks, scoreboard):
    """Main game loop."""
    game_is_on = True
    while game_is_on:
        sleep(ball.move_speed)
        screen.update()
        ball.move_ball()

        # Handle all possible collisions
        handle_collisions(ball, paddle, bricks, scoreboard)

        # End game if player reaches target score
        if scoreboard.break_points == 112:
            scoreboard.game_finished()
            game_is_on = False


if __name__ == "__main__":
    # screen setup
    screen = setup_screen()

    # Create game objects
    bricks = BrickManager()
    ball = Ball()
    scoreboard = BreakPoint()
    paddle = Paddle((0, -250))

    # Setup controls
    setup_controls(screen, paddle)

    # Start the game loop
    game_loop(screen, ball, paddle, bricks, scoreboard)

    # Exit on click
    screen.exitonclick()
