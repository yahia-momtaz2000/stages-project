import random
from turtle import Turtle, Screen

my_turle = Turtle()
my_turle.shape('turtle')
colors_list = ['red', 'green', 'blue', 'yellow', 'darkgreen']
angles_list = [0, 90, 180, 270]

my_turle.pensize(5)
my_turle.speed('slowest')

for i in range(200):
    my_turle.color(random.choice(colors_list))
    my_turle.forward(30)
    my_turle.setheading(random.choice(angles_list))


my_screen = Screen()
my_screen.exitonclick()
