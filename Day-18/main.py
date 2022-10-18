import turtle
import random
from turtle import Turtle, Screen
turtle.colormode(255)


# import colorgram
# colors = colorgram.extract('image.jpg', 35)
#
# color_tuple = []
#
# for item in colors:
#     list = item.rgb
#     new_color = (list.r, list.g, list.b)
#     color_tuple.append(new_color)
#
# print(color_tuple)



color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202),
              (112, 139, 141), (254, 194, 0), (134, 163, 184), (197, 92, 73), (47, 121, 86),]


def pick_color():
    global color_list
    a = random.choice(color_list)
    return a


timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.color("coral")
timmy.hideturtle()

x = -240
y = -240

for i in range(10):
    timmy.penup()
    timmy.setpos(x, y)
    for _ in range(10):

        timmy.penup()
        timmy.color(pick_color())
        timmy.dot(20)
        timmy.fd(50)
    y += 50







my_screen.exitonclick()