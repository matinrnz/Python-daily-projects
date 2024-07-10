from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    new_timmy = Turtle(shape="turtle")
    new_timmy.color(colors[i])
    new_timmy.penup()
    new_timmy.goto(x=-230, y=-100 + i * 40)
    all_turtles.append(new_timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for timmy in all_turtles:
        if timmy.xcor() > 230:
            is_race_on = False
            winning_color = timmy.pencolor()
            if winning_color == user_bet:
                print(f"You've win! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        timmy.forward(rand_distance)

screen.exitonclick()

