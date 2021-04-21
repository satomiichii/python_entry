from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('orange')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-275, 275)
        y_axis = random.randint(-275, 275)
        self.goto(x_axis, y_axis)
