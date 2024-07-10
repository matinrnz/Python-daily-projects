# # Extract colors from an image.
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('hirst_spot_image.jpg', 21)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# Create a hist painting
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(245, 151, 61), (139, 50, 104), (164, 168, 39), (242, 80, 58), (221, 238, 233), (250, 227, 232), (6, 140, 52), (241, 101, 161), (239, 66, 139), (4, 142, 183), (50, 201, 224), (160, 57, 53), (20, 164, 126), (247, 225, 40), (254, 231, 0), (211, 236, 239), (35, 192, 214), (119, 183, 149), (235, 166, 193), (239, 172, 157)]
timmy = Turtle()
screen = Screen()
# First method
# timmy.speed("fastest")
# timmy.shape("circle")
# timmy.color("white")
# timmy.fillcolor("white")
# timmy.pensize(20)
# TURTLE_SIZE = 20
# print(screen.window_width())
# x = TURTLE_SIZE * 6 - screen.window_width()/2
# y = -screen.window_height()/2 + TURTLE_SIZE * 6
# for _ in range(10):
#     timmy.penup()
#     timmy.goto(x, y)
#     timmy.pendown()
#     for i in range(10):
#         timmy.pencolor(random.choice(color_list))
#         timmy.forward(0)
#         timmy.penup()
#         timmy.forward(50)
#         timmy.pendown()
#     y += 50

# Second method
timmy.hideturtle()
timmy.setheading(225)
timmy.speed("fastest")
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
num_dots = 100
for dot_count in range(1, num_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()

