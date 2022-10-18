from turtle import Screen
import time
from snake import Snake
from snakefood import Food
from scoreboard import ScoreBoard

BOUNDARY = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

sb = ScoreBoard()

tim = Snake()
food = Food()


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.2)
    tim.move_fd()

    screen.onkey(tim.up, "Up")
    screen.onkey(tim.down, "Down")
    screen.onkey(tim.left, "Left")
    screen.onkey(tim.right, "Right")
    screen.listen()

    # detect collision with food
    if tim.head.distance(food) < 15:
        print("yummy")
        food.print_food()
        sb.add_score()
        tim.extend()

    # Detect collision with wall
    if tim.head.xcor() > BOUNDARY or tim.head.xcor() < -BOUNDARY or tim.head.ycor() < -BOUNDARY or tim.head.ycor() >\
            BOUNDARY:
        game_is_on = False
        sb.game_is_over()

    # Detect collision with tail
    for segment in tim.body[1:]:
        if tim.head.distance(segment) < 10:
            game_is_on = False
            sb.game_is_over()

screen.exitonclick()
