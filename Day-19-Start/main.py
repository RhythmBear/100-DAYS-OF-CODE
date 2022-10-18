import turtle
from turtle import Turtle, Screen
from prettytable import PrettyTable
import random
screen = Screen()
screen.setup(width=500, height=400)

#draw track
refree = Turtle()

refree.penup()
refree.setpos(250,200)
refree.right(90)
refree.pendown()
for _ in range(2):
    refree.fd(400)
    refree.right(90)
    refree.fd(500)
    refree.right(90)



# Race participants
red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
indigo = Turtle()
violet = Turtle()

racers = [red, orange, yellow, green, blue, indigo, violet]
race_list = ["red", "orange", 'yellow', 'green', 'blue', 'indigo', 'violet']


red.color('red')
orange.color("orange")
yellow.color("yellow")
green.color("green")
blue.color("blue")
indigo.color("indigo")
violet.color("purple")

red.shape('turtle')
orange.shape('turtle')
yellow.shape('turtle')
green.shape('turtle')
blue.shape('turtle')
indigo.shape('turtle')
violet.shape('turtle')

# send the racers to their positions
x = -250
y = -150
for racer in racers:
    racer.penup()
    racer.setpos(x, y)
    y += 50

start_race = False
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race?")


def check_bet():
    for racer in race_list:
        if user_bet == racer:
            return True
    return "Invalid input"


def move():
    return random.randint(1, 9)


if check_bet() == True:
    start_race = True

# Move the racers at varying paces till they get to the finish line

race_timer = [red, orange, yellow, green, blue, indigo, violet]
race_result = []
while start_race:
    for racer in race_timer:
        racer.fd(move())
    for racer in race_timer:
        if racer.xcor() >= 230.0:
            racer.fd(50)
            race_result.append(racer)
            race_timer.remove(racer)

        if len(race_timer) == 0:
            start_race = False
race_rank = []
for i in race_result:
    race_rank.append((i.color()))
print("\n")

if user_bet == race_rank[0][0]:
    print("You win!")
    print(f"Your {user_bet} turtle won.")
else:
    print("You loose")
    print(f"The {race_rank[0][0]} turtle won.")

print("\n")
print("********RANKINGS*********")
table = PrettyTable()
table.add_column("First place",  ["Second place", "Third place", "Fourth place", "Fifth place", "Sixth place", "Seventh place"])
table.add_column(f"{race_rank[0][0]}", [race_rank[1][0], race_rank[2][0], race_rank[3][0], race_rank[4][0], race_rank[5][0], race_rank[6][0]])
print("\n")
print(table)
screen.exitonclick()