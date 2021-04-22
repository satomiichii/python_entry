from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color('white')
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.display_score()