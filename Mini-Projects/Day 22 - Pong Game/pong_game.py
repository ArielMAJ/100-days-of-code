from my_global_constants import WIDTH, HEIGHT, GAME_SPEED
from paddle import *
from time import sleep
from ball import Ball
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Pong Game")

    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    screen.listen()

    player01 = Paddle(1)
    player02 = Paddle(2)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.update()

    screen.onkeypress(fun=player01.up_key, key='w')
    screen.onkeypress(fun=player01.down_key, key='s')

    screen.onkeypress(fun=player02.up_key, key='Up')
    screen.onkeypress(fun=player02.down_key, key='Down')

    keep_playing = True
    loop_counter = 0
    while keep_playing:
        if loop_counter % 50 != 0:
            ball.change_direction_if_hit_side_wall()
            ball.change_direction_if_hit_players(player01, player02)
            ball.check_score_and_restart_ball(scoreboard)
        ball.move()

    #     if player01.head.distance(food) < 15:
    #         food.rnd_position()
    #         scoreboard.update_score()
    #         player01.add_segment()
    #     x, y = player01.head.position()
    #
        sleep(GAME_SPEED)

        screen.update()
        loop_counter += 1
        if scoreboard.player01 >=5 or scoreboard.player02 >= 5:
            keep_playing = False
    #
    #     keep_playing = not player01.hit_the_wall() and not player01.hit_itself()
    #
    scoreboard.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()
