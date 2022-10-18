from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score()

    def score(self):
        self.goto(100, 170)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

        self.goto(-100, 170)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))

    def update(self):
        self.clear()
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("  GAME OVER! ", align="center", font=("courier", 30, "normal"))
