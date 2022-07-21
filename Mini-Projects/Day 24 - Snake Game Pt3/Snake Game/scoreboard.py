from turtle import Turtle
from my_global_constants import ALIGN, FONT, Y_WALL
import os


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.file_path = 'score.txt'
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.high_score = int(file.readline())
        else:
            self.high_score = 0

        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed(0)
        self.goto(0, Y_WALL)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        if self.high_score < self.score:
            self.high_score = self.score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.high_score <= self.score:
            self.high_score = self.score
            with open(self.file_path, 'w') as file:
                file.write(str(self.high_score))
        self.score = -1

        self.update_score()

