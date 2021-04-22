import time
from turtle import Screen
from center_line import CenterLine
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0)

center = CenterLine()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

right_score = ScoreBoard((90, 245))
left_score = ScoreBoard((-90, 245))

ball = Ball()

screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

game_is_on = True
ball_speed = 0.060

while game_is_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() < -275 or ball.ycor() > 280:
        ball.bounce('y')

    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325:
        ball.bounce('x')

    # detect collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce('x')

    # if the ball touch the right side wall, reset the ball position
    if ball.xcor() > 410:
        ball_speed *= 0.95
        left_score.update_score()
        ball.reset_ball()
        time.sleep(0.75)

    # if the ball touch the right side wall, reset the ball position
    if ball.xcor() < -410:
        ball_speed *= 0.95
        right_score.update_score()
        ball.reset_ball()
        time.sleep(0.75)

screen.exitonclick()
