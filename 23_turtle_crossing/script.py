import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
level = Scoreboard()
car_system = CarManager()

screen.listen()
screen.onkey(turtle.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_system.run_system()

    # Detect collision with the top wall
    if turtle.ycor() > turtle.finish:
        time.sleep(0.5)
        turtle.reset()
        level.level_up()
        car_system.speed_up()

    # Detect Collision with cars
    for car in car_system.group:
        if turtle.distance(car) < 30 and car.ycor() - turtle.ycor() < 20 :
            game_is_on = False


screen.exitonclick()
