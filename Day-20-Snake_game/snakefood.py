import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("blue")
        self.speed("fastest")
        self.print_food()

    def print_food(self):
        new_x = random.randint(-200, 200)
        new_y = random.randint(-200, 200)
        self.goto(new_x, new_y)
