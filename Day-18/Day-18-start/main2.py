import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)


timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.speed(0)

def get_color():

    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for _ in range(72):
    timmy.circle(100)
    timmy.color(get_color())
    timmy.right(5)



my_screen.exitonclick()

