from turtle import Turtle
from my_global_constants import ALIGN, FONT, Y_WALL


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed(0)
        self.goto(0, Y_WALL*.95)
        # self.score = -1
        self.player01 = 0
        self.player02 = 0
        self.update_score(0)

    def update_score(self, player):
        self.clear()
        if player == 1:
            self.player01 += 1
        elif player == 2:
            self.player02 += 1

        self.write(f"{self.player01} | {self.player02}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGN, font=FONT)
