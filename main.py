from turtle import Turtle, Screen
import random
screen = Screen()


colour = ["red","blue","green","black","purple","orange"]
y_pos = [-90,-60,-30,0,30,60]
screen.setup(width= 500,height=500)
all_turtle = []
user_bet = screen.textinput("Give your bet", "Which one do you choose ?")
game_is_on = False


for turtle_index in range(0,6):
    new_tim  = Turtle(shape='turtle')
    new_tim.color(colour[turtle_index]) 
    new_tim.penup()
    new_tim.goto(-230,y_pos[turtle_index])
    all_turtle.append(new_tim)

if user_bet:
    game_is_on = True   

while game_is_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game_is_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won the Game and the winner is {winning_color} turtle")

            else:
                print(f"You lost the game the winner is {winning_color} turtle")

        new_dist = random.randint(0,10)
        turtle.forward(new_dist)

screen.exitonclick()
