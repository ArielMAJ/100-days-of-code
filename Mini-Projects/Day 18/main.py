# from turtle import Turtle, Screen
# from get_tk_colors import colors_list
# import random as rnd
# import turtle
from my_turtle import MyTurtleClass, Screen
from time import sleep
import colorgram

def challenge_one(turtle):
    """Draw a square."""
    turtle.write_at_top("Challenge one.")

    turtle.random_shape()
    turtle.truly_random_color()

    turtle.jump_to(-50, 50)

    turtle.square()

    sleep(2)
    turtle.clear()


def challenge_two(turtle):
    """Draw a dashed line."""
    turtle.write_at_top("Challenge two.")

    turtle.random_shape()
    turtle.truly_random_color()

    turtle.jump_to(0, -150)

    turtle.left(90)
    turtle.dashed_line(300)
    turtle.right(90)

    sleep(2)
    turtle.clear()


def challenge_three(turtle):
    """Draw many polygons with different colors."""
    turtle.write_at_top("Challenge three.")
    timmy.jump_to(-50, 200)

    speed = turtle.speed()
    turtle.speed(0)
    turtle.draw_n_polygons(15)
    turtle.speed(speed)

    sleep(2)
    turtle.clear()


def challenge_four(turtle):
    """Random walk with different colors per sprint and increasing speed of turtle&WIDTH of pen."""
    turtle.write_at_top("Challenge four.")
    turtle.jump_to(0,0)

    turtle.random_walk()

    sleep(2)
    turtle.clear()


def challenge_five(turtle):
    turtle.write_at_top("Challenge five.")

    turtle.spirograph()

    sleep(2)
    turtle.clear()


def challenge_six(turtle):
    colors = colorgram.extract('image.jpg', 10)

    rgb_colors = [tuple(color_value for color_value in color.rgb) for color in colors]
    rgb_colors = [color for color in rgb_colors if sum(color) <= 720]
    turtle.spot_painting(rgb_colors)


timmy = MyTurtleClass()

challenge_one(timmy)
challenge_two(timmy)
challenge_three(timmy)
challenge_four(timmy)
challenge_five(timmy)
challenge_six(timmy)


screen = Screen()
screen.exitonclick()
