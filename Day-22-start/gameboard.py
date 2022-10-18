from turtle import Turtle


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        # Draw Border lines on top and below
        self.penup()
        self.pencolor('white')
        self.pensize(20)
        self.goto(-390, 300)
        self.pendown()
        self.fd(780)
        self.penup()
        self.goto(-390, -300)
        self.pendown()
        self.fd(780)
        self.hideturtle()
        self.pensize(5)

        self.fillcolor('green')
        self.penup()
        self.goto(-400, 300)
        self.setheading(270)
        self.begin_fill()
        self.pendown()
        self.fd(600)
        self.setheading(0)
        self.fd(800)
        self.setheading(90)
        self.fd(600)
        self.setheading(180)
        self.fd(800)
        self.end_fill()

        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.pensize(5)

        for _ in range(15):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
