from turtle import Turtle

STARTING_POS_X = -300
STARTING_POS_Y = -250


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.draw()

    def draw(self):
        global STARTING_POS_Y, STARTING_POS_X

        for _ in range(11):
            self.goto(STARTING_POS_X, STARTING_POS_Y)
            self.setheading(0)
            for i in range(12):
                self.pendown()
                self.fd(25)
                self.penup()
                self.fd(25)

            STARTING_POS_Y += 50
