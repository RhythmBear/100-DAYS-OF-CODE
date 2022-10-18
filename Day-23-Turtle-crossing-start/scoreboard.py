from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.current_level = 1
        self.print_level()

    def print_level(self):
        self.penup()
        self.clear()
        self.goto(-225, 265)
        self.write(f"Level: {self.current_level}",  align="center", font=FONT)
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.current_level += 1
        self.print_level()

    def game_is_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!! ", align="center", font=FONT)
