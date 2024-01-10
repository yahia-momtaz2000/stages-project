#
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.speed('slowest')


# forward
my_turtle.forward(300)

# backward
my_turtle.backward(150)

# right
my_turtle.right(90)
my_turtle.forward(100)

# left
my_turtle.left(90)
my_turtle.forward(100)

# penup
my_turtle.penup()
my_turtle.left(90)
my_turtle.forward(100)

# pendown
my_turtle.pendown()
my_turtle.forward(100)

# filcolor, beginfill, endfill
my_turtle.color('red')
my_turtle.fillcolor('green')
my_turtle.begin_fill()
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.end_fill()

# setheading    : 0, 90, 180, 270

# my_turtle.setheading(0) # east
# my_turtle.setheading(90) # = North
# my_turtle.setheading(180) #  = west
# my_turtle.setheading(270) # = south

# goto(x, y)
my_turtle.penup()
my_turtle.goto(-200, 0)

# shape : turtle, arrow, classic, circle, square
my_turtle.shape('square')

# dot
my_turtle.dot()
my_turtle.forward(100)
my_turtle.dot()
my_turtle.forward(100)

# stamp
my_turtle.stamp()
my_turtle.forward(100)
my_turtle.stamp()
my_turtle.forward(100)

my_screen = Screen()
my_screen.exitonclick()