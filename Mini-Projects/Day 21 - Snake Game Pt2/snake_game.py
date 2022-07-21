from my_global_constants import WIDTH, HEIGHT, GAME_SPEED
from my_snake import *
from time import sleep
from food import Food
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Snake Game")

    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    screen.listen()

    snake = SnakeClassForSnakeGame()
    food = Food()
    scoreboard = Scoreboard()

    screen.onkeypress(fun=snake.left_key, key='a')
    screen.onkeypress(fun=snake.up_key, key='w')
    screen.onkeypress(fun=snake.right_key, key='d')
    screen.onkeypress(fun=snake.down_key, key='s')

    screen.onkeypress(fun=snake.left_key, key='Left')
    screen.onkeypress(fun=snake.up_key, key='Up')
    screen.onkeypress(fun=snake.right_key, key='Right')
    screen.onkeypress(fun=snake.down_key, key='Down')

    keep_playing = True
    while keep_playing:
        snake.move()

        sleep(GAME_SPEED)
        if snake.head.distance(food) < 15:
            food.rnd_position()
            scoreboard.update_score()
            snake.add_segment()
        x, y = snake.head.position()

        screen.update()

        keep_playing = not snake.hit_the_wall() and not snake.hit_itself()

    scoreboard.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()
