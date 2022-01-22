from my_snake import *
from time import sleep

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Snake Game")
    width, height = 600, 600

    screen.setup(width=width, height=height)
    screen.tracer(0)
    screen.listen()

    snake = SnakeClassForSnakeGame()
    screen.update()

    screen.onkeypress(fun=snake.right_key, key='d')
    screen.onkeypress(fun=snake.right_key, key='Right')
    screen.onkeypress(fun=snake.left_key, key='a')
    screen.onkeypress(fun=snake.left_key, key='Left')

    for i in range(20):
        snake.move()

        sleep(.1)
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
