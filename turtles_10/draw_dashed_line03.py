from turtle import Turtle, Screen

my_turle = Turtle()
my_turle.shape('turtle')
my_turle.color('red')

# draw a dashed line
for i in range(10):
    my_turle.forward(10)
    my_turle.penup()
    my_turle.forward(10)
    my_turle.pendown()


my_screen = Screen()
my_screen.exitonclick()