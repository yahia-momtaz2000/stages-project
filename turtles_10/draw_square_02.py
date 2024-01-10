import math
from turtle import Turtle, Screen # from module import class, class


my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('red')

for _ in range(4):
    my_turtle.forward(200)
    my_turtle.right(90)

my_screen = Screen()
my_screen.exitonclick()