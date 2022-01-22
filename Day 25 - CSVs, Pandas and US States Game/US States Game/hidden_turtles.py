from turtle import Turtle


class TurtleWriter(Turtle):
    """Same as Turtle class, but with different default shape/color/speed and pen up."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()

