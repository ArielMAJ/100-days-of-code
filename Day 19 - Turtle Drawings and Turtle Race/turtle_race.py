from my_turtle import *


def main():
    screen = Screen()
    height = 600
    width = 800
    screen.setup(width=width, height=height)
    writer = MyTurtleClass()
    writer.hideturtle()
    writer.penup()

    user_bet = screen.textinput(title="Make your bet", prompt ="Which turtle will win the race? Enter a color: ").lower()

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    y = .45*height
    turtles = [MyTurtleClass(color=color) for color in colors]
    step = height/len(turtles)

    for turtle in turtles:
        # turtle.speed(0)
        turtle.penup()
        turtle.goto(x=-.9*(width/2), y=y)
        y -= step

    winner_color = ''
    while winner_color == '':
        for turtle in turtles:
            turtle.forward(rnd.randint(0, 30))
            if turtle.position()[0] >= .9*(width/2):
                winner_color = turtle.color()
                break



    if winner_color[0] == user_bet:
        writer.write_at_top(text=f"The winner was {winner_color[0]}. You've bet on {user_bet}.\nCongratulations, you got it right!", x=-.9 * width / 2, y=.80 * height / 2)
    else:
        writer.write_at_top(text=f"The winner was {winner_color[0]}. You've bet on {user_bet}.\nYou got it wrong. Good luck next time!", x=-.9 * width / 2, y=.8 * height / 2)

    screen.exitonclick()

if __name__ == "__main__":
    main()