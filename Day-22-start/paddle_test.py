from turtle import Turtle

STARTING_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle = []
        self.create_paddle()
        self.head = self.paddle[0]
        self.tail = self.paddle[-1]

    def create_paddle(self):
        for pos in STARTING_POSITIONS:
            pad_seg = Turtle()
            pad_seg.color('white')
            pad_seg.shape('square')
            pad_seg.penup()
            pad_seg.goto(pos)
            self.paddle.append(pad_seg)

    def move_up(self):

        for i in range((len(self.paddle) - 1), 0, -1):
            new_x = self.paddle[i - 1].xcor()
            new_y = self.paddle[i - 1].ycor()

            self.paddle[i].goto(new_x, new_y)

        new_y_cor = self.head.ycor() + 20
        self.head.goto(350, new_y_cor)

    def move_down(self):

        for i in range(0, (len(self.paddle) - 1)):
            new_x = self.paddle[i + 1].xcor()
            new_y = self.paddle[i + 1].ycor()

            self.paddle[i].goto(new_x, new_y)

        new_y_cor = self.tail.ycor() - 20
        self.tail.goto(350, new_y_cor)
