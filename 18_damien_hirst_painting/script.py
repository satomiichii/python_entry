from turtle import Turtle, Screen
import random
import colorgram

# rgb_list = []
# color_list = colorgram.extract('dot_art.jpeg', 30)
#
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))
#
# print(rgb_list)
color_list = [(245, 243, 238), (237, 240, 246), (201, 164, 112), (238, 246, 241), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51), (108, 127, 151)]

s = Turtle()
screen = Screen()
s.screen.colormode(255)
s.penup()
s.speed('fastest')
s.setheading(225)
s.forward(330)
s.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    s.dot(20, random.choice(color_list))
    s.forward(50)

    if dot_count % 10 == 0:
        s.setheading(90)
        s.forward(50)
        s.setheading(180)
        s.forward(500)
        s.setheading(0)


screen.exitonclick()