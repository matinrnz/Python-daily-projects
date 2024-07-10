from turtle import Turtle, Screen
import random as random

timmy = Turtle()
timmy.shape("circle")
timmy.color("cyan")
timmy.shapesize(0.5)
# timmy.pensize(20)
# timmy.speed(10)
directions = [0, 90, 180, 270]
timmy.pensize(1)
timmy.speed("fastest")
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]

# # Create a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # Draw a dashed line
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return timmy.color(r, g, b)


# # Draw a triangle, square, pentagon, hexagon,
# # heptagon, octagon, nonagon and decagon
# for num_sides in range(3, 11):
#     change_color()
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(360/num_sides)


# Draw a Random Walk
# for i in range(20):
#     steps = int(random.random() * 100)
#     angle = int(random.randint(0, 3) * 90)
#     timmy.right(angle)
#     timmy.fd(steps)
#     change_color()
# Dif
# for _ in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# # Using random colors
# for _ in range(200):
#     change_color()
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# Draw a Spirograph
for i in range(72):
    timmy.circle(100)
    # timmy.left(5)
    timmy.setheading(timmy.heading() + 5)
    change_color()

screen = Screen()
screen.exitonclick()

