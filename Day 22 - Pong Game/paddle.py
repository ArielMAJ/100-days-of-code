from turtle import Turtle, colormode, Screen
from my_global_constants import X_WALL, Y_WALL, PLAYER_SPEED
# import random as rnd

colormode(255)


class Paddle(Turtle):
    def __init__(self, player, shape='square', color='white'):
        super().__init__(shape=shape)
        self.player = player
        self.color(color)
        self.speed(0)
        self.penup()
        self.shapesize(stretch_wid=.8, stretch_len=4)
        self.setheading(90)

        if self.player == 1:
            self.goto(-X_WALL, 0)
        else:
            self.goto(X_WALL, 0)

    def up_key(self):
        if self.position()[1] <= Y_WALL*.9:
            self.forward(PLAYER_SPEED)

    def down_key(self):
        if self.position()[1] >= -Y_WALL*.9:
            self.backward(PLAYER_SPEED)

    # def hit_itself(self):
    #     for segment in self.snake[1:]:
    #         if self.head.distance(segment) <= 5:
    #             return True
    #     return False


