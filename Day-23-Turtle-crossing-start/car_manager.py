from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
MOVE_CONDITION = True


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.new_car()

    @staticmethod
    def get_color():
        return random.choice(COLORS)

    @staticmethod
    def y_pos():
        y_start = []

        for _ in range(-225, 275, 50):
            y_start.append(_)

        return random.choice(y_start)

    def new_car(self):
        self.penup()
        self.goto(330, self.y_pos())
        self.shape('square')
        self.shapesize(1, 2)
        a = self.get_color()
        self.color(a)
        self.setheading(180)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        new_y = self.ycor() + 0

        self.goto(new_x, new_y)

    @staticmethod
    def rand_num():
        return random.randint(4, 10)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
