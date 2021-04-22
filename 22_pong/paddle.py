from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.penup()

    def up(self):
        self.goto(y=self.ycor() + 20, x=self.xcor())

    def down(self):
        self.goto(y=self.ycor() - 20, x=self.xcor())
