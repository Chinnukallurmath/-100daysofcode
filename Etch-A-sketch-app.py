import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "y")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")

screen.exitonclick()