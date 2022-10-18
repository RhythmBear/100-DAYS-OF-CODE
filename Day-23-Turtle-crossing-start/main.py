import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

cars = []
car = CarManager()
p_1 = Player()
sb = Scoreboard()
track = Road()

screen.listen()
screen.onkey(p_1.move_forward, "Up")

sleep_time = 0.1
game_is_on = True

loop = 0
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    # Create New Cars and Add them to a list
    if loop % 10 == 0:
        for i in range(1, random.randint(2, 3)):
            new_car = CarManager()
            cars.append(new_car)

    # MOVe all the cars in the list
    for i in cars:
        i.move()

    # Check if the turtle has gotten to the top of the screen
    if p_1.ycor() >= 280:
        p_1.reset()
        sb.level_up()
        sleep_time *= 0.5
        car.level_up()

    # Check if the car has gone out of the screen so that you can remove it from the list
    for i in cars:
        if i.xcor() <= -350:
            cars.remove(i)
            del i

    # Check for collision
    for i in cars:
        if i.distance(p_1) <= 28:
            if 18 >= p_1.ycor() - i.ycor() >= 0:
                game_is_on = False
            elif 18 >= i.ycor() - p_1.ycor() >= 0:
                game_is_on = False
    loop += 1

sb.game_is_over()

screen.exitonclick()
