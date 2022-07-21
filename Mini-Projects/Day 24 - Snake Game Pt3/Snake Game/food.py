from turtle import Turtle
import random as rnd
from my_global_constants import X_WALL, Y_WALL


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color('blue')
        self.speed(0)
        self.rnd_position([])

    def rnd_position(self, snake):
        rnd_x = rnd.randint(10 - X_WALL, -10 + X_WALL) // 20 * 20
        rnd_y = rnd.randint(10 - Y_WALL, -10 + Y_WALL) // 20 * 20
        self.goto(rnd_x, rnd_y)

        for segment in snake:
            if self.distance(segment.position()) < 5:
                return self.rnd_position(snake)
