from turtle import Turtle, Screen

my_turle = Turtle()
my_turle.shape('turtle')
my_turle.color('red')

for i in range(11):
    my_turle.circle(100)
    current_heading = my_turle.heading()
    my_turle.setheading(current_heading + 10)


my_screen = Screen()
my_screen.exitonclick()