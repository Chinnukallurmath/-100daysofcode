import turtle
from turtle import Turtle
import random

turtle.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
color_list = [(34, 23, 13),(62, 73, 82),(57, 73, 42),(40, 98, 25),(13, 62, 99),(79, 20, 50),(66, 98, 28),(20, 77, 25),(82, 71, 85)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


turtle.done()