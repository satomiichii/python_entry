import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(310, random.randint(-260, 260))


class CarManager:
    def __init__(self):
        self.pace = STARTING_MOVE_DISTANCE
        self.group = []
        self.traffic = 6

    def generate_car(self):
        ran_num = random.randint(0, self.traffic)
        if ran_num == 0 or ran_num == 1:
            new_car = Car()
            self.group.append(new_car)

    def drive(self):
        for car in self.group:
            car.forward(self.pace)

    def speed_up(self):
        self.pace += MOVE_INCREMENT
        if self.traffic > 2:
            self.traffic -= 1

    def run_system(self):
        self.generate_car()
        self.drive()
