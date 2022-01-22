from turtle import Turtle, colormode, Screen
import random as rnd

colormode(255)


class SnakeClassForSnakeGame:
    def __init__(self):
        self.snake = [MyTurtle(), MyTurtle(x=-20), MyTurtle(x=-40)]

    def move(self):
        for segment_n in range(len(self.snake)-1, 0, -1):
            self.snake[segment_n].jump_to(self.snake[segment_n-1].position())
        self.snake[0].forward(20)

    def right_key(self):
        self.snake[0].setheading(self.snake[0].heading() - 90)

    def left_key(self):
        self.snake[0].setheading(self.snake[0].heading() + 90)


class MyTurtle(Turtle):
    def __init__(self, shape='square', color='white', x=0, y=0):
        super().__init__(shape=shape)
        if x != 0 or y != 0:
            self.jump_to((x, y))
        self.color(color)
        # self.movement = movement
        self.penup()
        #

    def random_shape(self):
        shape = rnd.choice(['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'])
        self.shape(shape)

    def random_color(self):
        r = rnd.randint(0, 255)
        g = rnd.randint(0, 255)
        b = rnd.randint(0, 255)

        self.color((r, g, b))

    def write_at_top(self, text, x=-50, y=250):
        if self.isvisible():
            was_visible = True
            self.hideturtle()
        else:
            was_visible = False

        self.color('black')
        go_back = self.position()
        self.jump_to((x, y))
        self.write(text, font=('Arial', 15, 'normal'))
        self.jump_to(*go_back)

        if was_visible:
            self.showturtle()

    def jump_to(self, position: tuple) -> None:
        """Jumps turtle to coordinate (x,y) without changing speed, orientation or pen-state.
This doesn't draw along the way"""
        speed = self.speed()

        self.speed(0)
        self.goto(position)
        self.speed(speed)


