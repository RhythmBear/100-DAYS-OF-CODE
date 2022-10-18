from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()

    def create_paddle(self, xcor, ycor):
        self.goto(xcor, ycor)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_r(self):
        self.create_paddle(380, 0)

    def reset_l(self):
        self.create_paddle(-380, 0)
