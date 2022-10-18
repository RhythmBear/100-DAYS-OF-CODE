import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()
my_screen = Screen()


timmy.shape("turtle")


def draw_3_to_10_side_shape():
    def get_color(i):
        c_list = ['MediumBlue', 'LimeGreen', 'Turquoise', 'DarkOliveGreen', 'Orange', 'Maroon', 'Yellow', 'Magenta']
        s_color = c_list[i]
        return s_color

    def draw_shape(num):
        for _ in range(num):
            timmy.forward(100)
            timmy.right(360 / num)

    for i in range(3, 11):
        color = get_color(i - 3)
        timmy.color(f"{color}")
        draw_shape(i)


#### Draw a random walk

turtle.colormode(255)

def get_color():

    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def turn():
    a = random.randint(0, 5)
    if a == 1:
        return timmy.setheading(180)
    elif a == 2:
        return timmy.setheading(90)
    elif a == 3:
        return timmy.setheading(270)
    elif a == 4:
        return timmy.setheading(0)


timmy.speed(0)

for _ in range(150):

    timmy.color(get_color())
    timmy.pensize(10)
    turn()
    timmy.forward(30)

my_screen.exitonclick()
