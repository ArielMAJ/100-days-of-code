from my_turtle import *


def main():
    screen = Screen()
    screen.setup(width=500, height=400)

    screen.listen()

    turtle = MyTurtleClass()
    screen.onkeypress(fun=turtle.up_key, key='w')
    screen.onkeypress(fun=turtle.down_key, key='s')
    screen.onkeypress(fun=turtle.right_key, key='d')
    screen.onkeypress(fun=turtle.left_key, key='a')
    screen.onkey(fun=turtle.clear_and_recenter, key='c')
    screen.onkey(fun=turtle.random_color, key='r')
    screen.onkey(fun=turtle.random_shape, key='t')
    screen.onkeypress(fun=turtle.increase_movement, key='+')
    screen.onkeypress(fun=turtle.decrease_movement, key='-')

    screen.exitonclick()

if __name__ == "__main__":
    main()