from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from gameboard import GameBoard
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Define game screen requirements
game_screen = Screen()
game_screen.tracer(0)
game_screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
game_screen.bgcolor('black')
game_screen.title("Ping Pong!")
end_game = game_screen.numinput("Point settings", "What score do you want to play to? ", minval=3, maxval=11)

# Draw Game board
board = GameBoard()
sb = ScoreBoard()

# Create Right and Left Paddle Object
r_paddle = Paddle()
r_paddle.create_paddle(380, 0)
l_paddle = Paddle()
l_paddle.create_paddle(-380, 0)
egg = Ball()

time.sleep(2)
game_is_on = True


def game_is_over():
    global game_is_on
    game_is_on = False


while game_is_on:
    game_screen.onkey(r_paddle.move_up, "Up")
    game_screen.onkey(r_paddle.move_down, "Down")
    game_screen.onkey(l_paddle.move_up, "w")
    game_screen.onkey(l_paddle.move_down, "s")
    game_screen.onkey(game_is_over, "t")

    game_screen.listen()
    game_screen.update()

    game_screen.update()
    time.sleep(egg.move_speed)

    egg.move()

    # Check for collision with the walls
    if egg.ycor() >= 280 or egg.ycor() <= -280:
        egg.bounce_y()

    # Check For collision with the paddles
    if egg.distance(r_paddle) < 50 and egg.xcor() >= 350 or egg.distance(l_paddle) < 50 and egg.xcor() <= -350:
        egg.bounce_x()
        egg.move_speed *= 0.5

    #  Check if the ball has gone past the goal line
    if egg.xcor() > 400:
        print(" Left paddle wins a point ")
        egg.start_over()
        time.sleep(1)
        r_paddle.reset_r()
        l_paddle.reset_l()
        egg.move_speed = 0.1
        sb.l_score += 1

        if sb.l_score == int(end_game):
            print("Left Player wins")
            game_is_on = False
        sb.update()

    if egg.xcor() < -400:
        print(" Right paddle wins a point ")
        egg.start_over()
        r_paddle.reset_r()
        l_paddle.reset_l()
        egg.move_speed = 0.1
        sb.r_score += 1
        if sb.r_score == int(end_game):
            print("Right Player wins")
            game_is_on = False
        sb.update()

        time.sleep(1)

sb.game_over()

game_screen.exitonclick()
