from turtle import Turtle, colormode, Screen
from my_global_constants import X_WALL, Y_WALL
import random as rnd

colormode(255)


class SnakeClassForSnakeGame:
    def __init__(self):
        self.snake = []
        self.add_segment()
        self.add_segment()
        self.add_segment()

        self.head = self.snake[0]
        self.last_position = self.head.position()

    def move(self):
        for segment_n in range(len(self.snake) - 1, 0, -1):
            self.snake[segment_n].goto(self.snake[segment_n - 1].position())
        self.last_position = self.head.position()
        self.head.forward(20)

    def have_moved(self):
        return self.last_position != self.head.position()

    def right_key(self):
        if self.head.heading() != 180 and self.have_moved():
            self.head.setheading(0)
            self.last_position = self.head.position()

    def left_key(self):
        if self.head.heading() != 0 and self.have_moved():
            self.head.setheading(180)
            self.last_position = self.head.position()

    def up_key(self):
        if self.head.heading() != 270 and self.have_moved():
            self.head.setheading(90)
            self.last_position = self.head.position()

    def down_key(self):
        if self.head.heading() != 90 and self.have_moved():
            self.head.setheading(270)
            self.last_position = self.head.position()

    def add_segment(self):
        try:
            x, y = self.snake[-1].position()
        except:
            x, y = 0, 0
        self.snake.append(MyTurtle(x=x, y=y))

    def hit_itself(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) <= 5:
                return True
        return False

    def hit_the_wall(self):
        x, y = self.head.position()
        return abs(x) >= X_WALL or abs(y) >= Y_WALL


class MyTurtle(Turtle):
    def __init__(self, shape='square', color='white', x=0.0, y=0.0):
        super().__init__(shape=shape)

        self.color(color)
        self.speed(0)
        self.penup()
        if x != 0 or y != 0:
            self.goto(x, y)
