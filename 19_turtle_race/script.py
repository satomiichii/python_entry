import random
from turtle import Turtle, Screen

turtle_color = ['red', 'orange', 'blue', 'green', 'purple', 'yellow']
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


for num in range(0, 6):
    index = num
    num = Turtle(shape='turtle')
    num.penup()
    num.color(turtle_color[index])
    num.goto(x=-230, y=150 - index * 60)
    all_turtles.append(num)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

