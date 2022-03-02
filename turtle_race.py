import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "yellow", "blue", "orange", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color([colors[turtle_index]])
    new_turtle.goto(x= -230, y= y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtule is the winner and you bet on {user_bet} turtle")
        rand_distance = random.randint(0,5)
        turtle.forward(rand_distance)

screen.exitonclick()
