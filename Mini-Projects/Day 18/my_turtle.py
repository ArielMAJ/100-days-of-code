from turtle import Turtle, Screen, colormode
import get_tk_colors
import random as rnd

colormode(255)


class MyTurtleClass(Turtle):
    def __init__(self):
        super().__init__()
        self.turtle_colors = get_tk_colors.colors_list()
        self.last_jump = (0,0)

    def random_shape(self):
        shape = rnd.choice(['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'])
        self.shape(shape)

    def random_color(self):
        color = rnd.choice(self.turtle_colors)
        self.color(color)
        print(color)

    def truly_random_color(self):
        r = rnd.randint(0, 255)
        g = rnd.randint(0, 255)
        b = rnd.randint(0, 255)

        self.color((r, g, b))

    def random_direction(self):
        directions = [0, 90, 180, 270]
        direction = rnd.choice(directions)
        self.setheading(direction)

    def write_at_top(self, text, x=-50, y=250):
        self.hideturtle()
        self.color('black')
        go_back = self.last_jump
        self.jump_to(x, y)
        self.write(text, font=('Arial', 15, 'normal'))
        self.jump_to(*go_back)
        self.showturtle()

    def forward_right(self, forward=100, right=90):
        """Receives a turtle objectand makes it go forward 100px and turn right 90º by default.
    You can pass in specific 'forward' and 'right' attributes."""
        self.forward(forward)
        self.right(right)

    def square(self):
        """Receives a turtle object and makes it draw a square."""
        [self.forward_right() for _ in range(4)]

    def dashed_line(self, total_px = 100, line_px = 10):
        """Draws a 'total_px' long dashed line with each dash and space being 'line_px' long."""
        for i in range(total_px//(2*line_px)):
            self.forward(line_px)
            self.penup()
            self.forward(line_px)
            self.pendown()

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

        self.last_jump = (x,y)

    def draw_n_polygons(self, n):
        if n >= 1 and type(n)==int:
            for polygon in range(3, 3 + n):
                self.random_shape()
                self.truly_random_color()
                self.jump_to(*self.last_jump)
                self.setheading(0)
                [self.forward_right(right=360/polygon) for _ in range(polygon)]
        else:
            print("Input not recognized. Please input a natural number.")

    def random_walk(self,steps=100):
        """Random walk with different colors per sprint and increasing speed of turtle&WIDTH of pen."""
        self.speed(1)
        # self.pensize(5)

        for step in range(steps):
            self.truly_random_color()
            self.random_shape()
            self.random_direction()
            self.forward(15)

            speed = self.speed()
            if speed<10 and rnd.random()>.95:
                self.speed(speed+1)
            if rnd.random()>.95:
                self.pensize(self.pensize()+1)
        self.pensize(1)

    def spirograph(self, radius=100, angle_per_circle=5):
        self.jump_to(0,0)
        self.setheading(0)
        self.speed(0)
        self.pensize(1)

        self.circle(radius)
        self.left(angle_per_circle)
        for _ in range(360//angle_per_circle):
            self.truly_random_color()
            self.circle(radius)
            self.left(angle_per_circle)

    def spot_painting(self, colors_list, x_dots=10, y_dots=10, step=50):
        self.hideturtle()
        self.speed(0)
        for y in range(0, y_dots * step, step):
            for x in range(0, x_dots * step, step):
                self.color(rnd.choice(colors_list))
                self.jump_to(x-250, y-250)
                self.dot(20)
        self.showturtle()
