from turtle import Turtle
import random as rnd

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape('turtle')
        self.draw_arena()
        self.color('green')
        self.showturtle()
        self.starting_position()
        # self.forward(30)

    def draw_arena(self):
        self.goto(300, -295)
        while self.ycor() < FINISH_LINE_Y-45:
            self.goto(300, self.ycor()+30)
            self.setheading(180)
            self.dashed_horizontal_line()

    def draw_arena(self):
        self.pensize(2)
        self.setheading(180)
        self.goto(300, -265)
        self.color('lightgreen')
        self.dashed_horizontal_line()
        self.color('black')
        while self.ycor() < FINISH_LINE_Y-75:
            self.goto(300, self.ycor()+30)

            self.dashed_horizontal_line()

        self.color('lightgreen')
        self.goto(300, self.ycor()+30)
        # self.setheading(180)
        self.dashed_horizontal_line()

    def dashed_horizontal_line(self):
        while self.xcor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(15)

    def up_key(self):
        self.goto(x=0, y=self.ycor()+MOVE_DISTANCE)
        # self.forward(30)

    def rnd_color(self):
        self.color(rnd.choice(COLORS))

    def starting_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

