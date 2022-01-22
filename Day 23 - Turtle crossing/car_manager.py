from turtle import Turtle
import random as rnd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = [self.create_car() for _ in range(7)]

    def random_start_position(self, car):
        car.goto(310, rnd.choice(list(range(-250, 250, 30))))

    def create_car(self):
        car = Turtle()
        car.color(rnd.choice(COLORS))
        car.penup()
        car.speed(0)
        car.shape('square')
        car.shapesize(stretch_wid=.8, stretch_len=1.5)
        self.random_start_position(car)
        car.setheading(180)
        car.movement_speed = STARTING_MOVE_DISTANCE * rnd.random()
        return car

    def run_cars(self):
        # while True:
        for car in self.cars:
            if car.xcor() < -300:
                if rnd.random() > .7:
                    self.cars.append(self.create_car())
                self.random_start_position(car)
            car.forward(car.movement_speed)

    def update_cars_speeds(self):
        for car in self.cars:
            car.movement_speed += MOVE_INCREMENT
