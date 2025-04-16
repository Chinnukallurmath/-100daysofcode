import random
import turtle
from turtle import *

screen = Screen()
screen.setup(width=500, height=400)

user_input = screen.textinput("turtle race", "Who can win here? : ")
colors = ["pink", "red", "green", "violet", "yellow"]
y_position = [0, 40, 80, 120, 160]
all_turtles = []

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 260)
scoreboard.write("Race is on!", align="center", font=("Arial", 18, "bold"))

for turtle_index in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        r_race = random.randint(0, 10)
        racer.forward(r_race)

        if racer.xcor() > 230:
            is_race_on = False

            scoreboard.clear()
            winning_color = racer.pencolor()
            if winning_color == user_input:
                scoreboard.write(f"you won! the winner is {winning_color}", align="center", font=("arial", 18, "bold"))
            else:
                scoreboard.write(f"you lose! the winner is {winning_color}", align="center", font=("arial", 18, "bold"))

screen.exitonclick()