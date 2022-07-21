from turtle import Turtle
import random as rnd
from my_global_constants import X_WALL, Y_WALL, BALL_SPEED, BALL_PLAYER_DIST


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_game_board()

        self.shapesize(stretch_wid=.85, stretch_len=.85)
        self.shape("circle")
        self.color('blue')
        self.new_round()

        # self.speed(1)

    def new_round(self):
        self.rnd_position()
        while self.heading() % 90 == 0:
            self.setheading(rnd.randint(1, 359))

    def rnd_position(self):
        # rnd_x = rnd.randint(100 - X_WALL, -100 + X_WALL)
        rnd_y = rnd.randint(50 - Y_WALL, -50 + Y_WALL)
        self.goto(0, rnd_y)

    def draw_game_board(self):
        line_px = 20
        self.color('white')
        self.speed(0)
        self.penup()
        self.goto(0, -Y_WALL)
        self.setheading(90)
        self.pensize(4)
        self.pendown()
        for i in range(int(Y_WALL*1.05//line_px)):
            self.forward(line_px)
            self.penup()
            self.forward(line_px)
            self.pendown()
        self.penup()
        self.goto(0, 0)

    def move(self):
        self.forward(BALL_SPEED)

    def change_direction_if_hit_side_wall(self):
        x, y = self.position()

        if abs(y) < Y_WALL:
            return
        elif self.heading() < 90 or self.heading() > 270:
            if y >= Y_WALL:
                self.setheading(360-self.heading()+rnd.randint(1, 5))
            elif y <= -Y_WALL:
                self.setheading(360-self.heading()-rnd.randint(1, 5))
            else:
                return
        else:
            if y >= Y_WALL:
                self.setheading(360-self.heading()-rnd.randint(1, 5))
            elif y <= -Y_WALL:
                self.setheading(360-self.heading()+rnd.randint(1, 5))
            else:
                return
        self.forward(BALL_SPEED/2)

    def check_score_and_restart_ball(self, scoreboard):
        x, y = self.position()
        if x >= X_WALL:
            self.new_round()
            scoreboard.update_score(player=1)
        elif x <= -X_WALL:
            self.new_round()
            scoreboard.update_score(player=2)
        else:
            return

    def change_direction_if_hit_players(self, *args):
        for player in args:
            if self.distance(player) <= BALL_PLAYER_DIST and abs(self.xcor()) > X_WALL*.9:
                if self.heading() < 180:
                    self.setheading(180-self.heading()+rnd.randint(-5, 5))
                    self.forward(BALL_SPEED/2)
                else:
                    self.setheading(360-self.heading()+180+rnd.randint(-5, 5))
                    self.forward(BALL_SPEED/2)
