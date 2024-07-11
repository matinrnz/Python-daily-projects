import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()


def check_answer():
    for state_name in states:
        if answer == state_name:
            write_on_map()
            return True


def write_on_map():
    state_info = (data[data.state == answer])
    x_value = int(state_info.x.values[0])
    y_value = int(state_info.y.values[0])
    pos = (x_value, y_value)
    writer_turtle.penup()
    writer_turtle.goto(pos)
    writer_turtle.write(answer, align="center")


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # states to learn
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn.csv")
        break
    if answer not in guessed_states:
        if check_answer():
            guessed_states.append(answer)

screen.exitonclick()
