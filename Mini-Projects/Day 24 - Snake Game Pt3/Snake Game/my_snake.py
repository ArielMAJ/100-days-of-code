from turtle import Turtle, colormode, Screen
from my_global_constants import X_WALL, Y_WALL
import random as rnd

colormode(255)


class SnakeClassForSnakeGame:
    """The name says it all."""
    def __init__(self):
        self.head = None
        self.last_position = None
        self.old_segments = []
        self.snake = []

        self.new_snake()

    def new_snake(self):
        """Creates a new snake. Hides old snake segments from previous rounds for later reuse."""
        for segment_pos in range(len(self.snake)-1, -1, -1):
            segment = self.snake.pop(segment_pos)
            segment.hideturtle()
            self.old_segments.append(segment)

        self.add_segment()
        self.add_segment()
        self.add_segment()

        self.head = self.snake[0]
        self.last_position = self.head.position()

    def move(self):
        """Moves each segment to the position of the segment ahead of it and moves the head segment one "cell"."""
        for segment_n in range(len(self.snake) - 1, 0, -1):
            self.snake[segment_n].goto(self.snake[segment_n - 1].position())
        self.last_position = self.head.position()
        self.head.forward(20)

    def have_moved(self):
        """Checks if the head have moved. This is to avoid the head turning into itself when pressing keys."""
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
        """Adds new segments to the snake. Reuses old segments from previous rounds when available."""
        try:
            x, y = self.snake[-1].position()
        except:
            x, y = 0, 0

        if len(self.old_segments) > 0:
            segment = self.old_segments.pop(0)
            segment.goto(x, y)
            segment.showturtle()
            self.snake.append(segment)
        else:
            self.snake.append(MyTurtle(x=x, y=y))

    def hit_itself(self):
        """Checks if the head has hit the body. Returns True if yes, else False."""
        for segment in self.snake[1:]:
            if self.head.distance(segment) <= 5:
                return True
        return False

    def hit_the_wall(self):
        """Checks if the head has hit one of the walls. Returns True if yes, else False."""
        x, y = self.head.position()
        return abs(x) >= X_WALL or abs(y) >= Y_WALL


class MyTurtle(Turtle):
    """Same as Turtle class, but with different default shape/color/speed and pen up."""
    def __init__(self, shape='square', color='white', x=0, y=0):
        super().__init__(shape=shape)

        self.color(color)
        self.speed(0)
        self.penup()
        if x != 0 or y != 0:
            self.goto(x, y)
