from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 7.5
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.current_pos = self.position()
        self.shape('turtle')
        self.color('cyan')
        self.reset()

    def reset(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.penup()
        self.fd(MOVE_DISTANCE)
