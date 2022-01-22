from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.speed(0)
        self.goto(-200, 267)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGN, font=FONT)
