from turtle import Turtle, colormode, Screen
import random as rnd

colormode(255)


class MyTurtleClass(Turtle):
    def __init__(self, shape='turtle', color='green', movement=10):
        super().__init__(shape=shape)
        self.color(color)
        self.last_jump = (0, 0)
        self.movement=movement

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
        go_back = self.last_jump
        self.jump_to(x, y)
        self.write(text, font=('Arial', 15, 'normal'))
        self.jump_to(*go_back)

        if was_visible:
            self.showturtle()

    def jump_to(self,x,y):
        """Jumps turtle to coordinate (x,y) without changing speed, orientation or pen-state.
This doesn't draw along the way"""
        speed = self.speed()

        was_down = self.isdown()

        if was_down:
            self.penup()

        self.speed(0)
        self.goto(x, y)
        self.speed(speed)

        if was_down:
            self.pendown()

        self.last_jump = (x, y)

    def up_key(self):
        self.forward(self.movement)

    def down_key(self):
        self.backward(self.movement)

    def right_key(self):
        self.right(self.movement)

    def left_key(self):
        self.left(self.movement)

    def clear_and_recenter(self):
        self.clear()
        self.jump_to(0, 0)
        self.setheading(0)

    def increase_movement(self):
        self.movement += 1

    def decrease_movement(self):
        self.movement -= 1
