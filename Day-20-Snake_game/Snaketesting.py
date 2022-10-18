from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for i in range(3):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(starting_positions[i])
    segments.append(new_segment)


def up():
    """Sets the snake heading to face the Top of the screen"""
    segments[0].setheading(90)


game_is_on = True


def move_now():
    num_of_loops = 0
    # while game_is_on:

    for _ in range(10):
        screen.update()
        time.sleep(0.5)

        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)

        segments[0].fd(20)

        num_of_loops += 1

        if num_of_loops == 5:
            up()


screen.onkey(move_now, "Up")
screen.listen()

screen.exitonclick()
