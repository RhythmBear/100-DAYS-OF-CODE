from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.body = []
        self.length = len(self.body)
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Returns a 3 segment snake unto the screen"""
        for position in STARTING_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.body.append(new_segment)

    def extend(self):
        pos = self.body[-1].position()
        self.create_segment(pos)

    def move_fd(self):
        """Moves the snake forward"""

        for i in range((len(self.body) - 1), 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()

            self.body[i].goto(new_x, new_y)

        self.head.fd(MOVING_DISTANCE)

    def up(self):
        """Sets the snake heading to face the Top of the screen"""
        if self.head.heading() != 270:
            self.body[0].setheading(90)

    def right(self):
        """Sets the snake heading to face the right of the screen"""
        if self.head.heading() != 180:
            self.body[0].setheading(0)

    def left(self):
        """Sets the snake heading to face the left of the screen"""
        if self.head.heading() != 0:
            self.body[0].setheading(180)

    def down(self):
        """Sets the snake heading to face the down of the screen"""
        if self.head.heading() != 90:
            self.body[0].setheading(270)
