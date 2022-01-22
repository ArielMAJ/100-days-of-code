import pandas as pd
from hidden_turtles import TurtleWriter
from turtle import Screen,onscreenclick,mainloop,addshape,shape
from time import sleep


WIDTH, HEIGHT = 800, 600
ALIGN = 'center'
FONT = ('Arial', 10, 'normal')
IMAGE = "blank_states_img.gif"

def get_mouse_click_coor():
    screen = Screen()
    turtle = TurtleWriter()
    addshape(IMAGE)
    shape(IMAGE)
    onscreenclick(lambda x, y: print(x, y))
    mainloop()


def main():
    us_states = pd.read_csv("50_states.csv")
    us_states_list = us_states.state.to_list()
    screen = Screen()
    screen.bgcolor("white")
    screen.title("US States Game")

    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgpic(IMAGE)

    turtle_state_writer = TurtleWriter()
    # turtle_attempt_writer = TurtleWriter()
    # turtle_attempt_writer.goto(x=WIDTH/2-100, y=HEIGHT/2-50)

    correct_guesses = 0
    # turtle_attempt_writer.write(f"Correct Guesses: {correct_guesses}", align=ALIGN, font=FONT)
    while correct_guesses < 50:
        guess = screen.textinput(title=f"Guess a state [{correct_guesses}/50].", prompt="Type the name of a state.").title()
        if guess == 'Exit':
            break
        elif guess in us_states_list:
            us_states_list.remove(guess)
            state = us_states[us_states.state == guess]
            turtle_state_writer.goto(int(state.x), int(state.y))
            us_states.drop(state.index[0], axis=0, inplace=True)
            turtle_state_writer.write(guess, align=ALIGN, font=FONT)
            correct_guesses += 1
            # turtle_attempt_writer.clear()
            # turtle_attempt_writer.write(f"Correct Guesses: {correct_guesses}", align=ALIGN, font=FONT)
            sleep(1)

    us_states.to_csv("states_to_learn.csv")

    screen.exitonclick()


if __name__ == "__main__":
    main()
    # get_mouse_click_coor()
