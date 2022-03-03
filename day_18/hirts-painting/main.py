# import colorgram
# import random

import turtle

turtle.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
#               (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
#               (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
#               (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
#               (176, 192, 208), (168, 99, 102)]


def do_line(size):
    for _ in range(size):
        tim.color(color)
        tim.dot(30, color)
        tim.penup()
        tim.forward(60)


def start_line():
    tim.right(90)
    tim.penup()
    tim.forward(60)
    tim.right(90)
    tim.forward(900)


screen = turtle.Screen()
turtle.bgcolor(0, 0, 0)
tim = turtle.Turtle()
tim.penup()
tim.left(150)
tim.forward(500)
tim.setheading(0)

for ind in range(9):
    tim.speed(20)
    if ind < 3:
        color = (255, 255, 255)
    elif ind < 6:
        color = (43, 185, 0)
    else:
        color = (255, 0, 0)
    do_line(15)
    start_line()
    tim.left(180)

screen.exitonclick()
