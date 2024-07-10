from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_rights():
    timmy.right(10)
    timmy.forward(10)


def move_lefts():
    timmy.left(10)
    timmy.forward(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_rights)
screen.onkey(key="a", fun=move_lefts)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

