from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 300)
        self.setheading(270)
        self.pensize(7)
        self.color('white')
        self.hideturtle()
        self.draw_line()

    def draw_line(self):
        for x in range(16):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
