from turtle import Turtle, Screen

s = Turtle()
screen = Screen()


def forwards():
    s.forward(10)


def backwards():
    s.backward(10)


def clockwise():
    s.right(10)


def counter_clockwise():
    s.left(10)


def clear():
    s.reset()


screen.listen()
screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
