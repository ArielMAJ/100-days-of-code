import time
import turtle
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
little_turtle = Player()
screen.listen()

screen.onkey(fun=little_turtle.up_key, key='Up')
# screen.onkeypress(fun=little_turtle.rnd_color, key='c')

car_manager = CarManager()

game_is_on = True
while game_is_on:
    if little_turtle.ycor() >= FINISH_LINE_Y:
        little_turtle.starting_position()
        scoreboard.update_score()
        car_manager.update_cars_speeds()

    for car in car_manager.cars:
        if car.ycor() == little_turtle.ycor() and little_turtle.distance(car) < 20:
            game_is_on = False

    car_manager.run_cars()
    # car_manager.forward(20)
    time.sleep(0.03)
    screen.update()
    # little_turtle.forward(5)

scoreboard.game_over()
screen.exitonclick()
