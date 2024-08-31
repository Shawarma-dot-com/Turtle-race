import random
from turtle import Turtle, Screen



screen = Screen()
screen.setup(500, 400)
is_on = False
colour = ["red", "orange", "blue", "purple"]
y_position = [-150, -50, 50, 150]
all_turtle = []

for turtle_index in range(0, 4):

    y = y_position[turtle_index]
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colour[turtle_index])
    tim.goto(-230, y)
    all_turtle.append(tim)
user_bet = screen.textinput("Make your bet", "Which colour turtle do you think will win: ")

if user_bet:
    is_on = True
else:
    is_on = False

while is_on:
    for tim in all_turtle:
        if tim.xcor() > 230:
            is_on = False
            winning_tim = tim.pencolor()
            if winning_tim == user_bet:
                print(f"You won the {winning_tim} Turtle is the winner")
            else:
                print(f"You lost the {winning_tim} Turtle won")

        rand_distance = random.randint(0, 10)
        tim.forward(rand_distance)

screen.exitonclick()
