import random
from turtle import Turtle, Screen

my_turle = Turtle()
my_turle.shape('turtle')


# pentagon = 5 sides
colors_list = ['red', 'green', 'blue', 'yellow', 'darkgreen']

for i in range(3, 11):
    num_of_sides = i
    my_turle.color(random.choice(colors_list))
    angle = 360 / num_of_sides
    for j in range(i):
        my_turle.forward(100)
        my_turle.left(angle)



my_screen = Screen()
my_screen.exitonclick()