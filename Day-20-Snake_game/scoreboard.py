from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor('white')
        self.current_score = 0
        self.write(f"Score = {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_is_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score = {self.current_score}", align='center', font=('Arial', 12, 'normal'))
