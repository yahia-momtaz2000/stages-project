import random
from turtle import Turtle, Screen
import time

def draw_turtle(t_name, t_color, t_y):
    t_name = Turtle()
    t_name.color(t_color)
    t_name.shape('turtle')
    t_name.shapesize(1.5)
    t_name.penup()
    t_name.goto(-300, t_y)
    t_name.pendown()
    t_name.speed('slowest')
    return t_name


game_end = False
def move_func():
    if not game_end:
        green_turtle.forward(10)

# main program
my_turtle = Turtle()

# Screen setup
my_screen = Screen()
my_screen.title("Race Game")
my_screen.setup(800, 500)
my_screen.bgcolor("forestgreen")




# Heading
my_turtle.penup()
my_turtle.goto(-100, 205)
my_turtle.color('White')
my_turtle.write('Turtle race', font=('Arial', 20, 'bold'))

# The Floor
my_turtle.goto(-350, 200)
my_turtle.pendown()
my_turtle.color('chocolate')
my_turtle.begin_fill()
my_turtle.speed('slow')
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()
my_turtle.color('white')

# The Finish Line
gap_size = 20
my_turtle.shape('square')
my_turtle.penup()


# White Square Row 1
my_turtle.color('white')
for i in range(10):
    my_turtle.goto(250, (170 - (i * gap_size * 2)))
    my_turtle.stamp()

# White Square Row 2
for i in range(10):
    my_turtle.goto(250 + gap_size, (190 - (i * gap_size * 2)))
    my_turtle.stamp()

# Blacks Square Row 1
my_turtle.color('black')
for i in range(10):
    my_turtle.goto(250, (190 - (i * gap_size * 2)))
    my_turtle.stamp()


# Blacks Square Row 2
my_turtle.color('black')
for i in range(10):
    my_turtle.goto(250 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    my_turtle.stamp()


# Turtle 1 - Blue
blue_turtle = draw_turtle(t_name='blue_turtle', t_color='cyan', t_y=150)
"""
blue_turtle = Turtle()
blue_turtle.color('cyan')
blue_turtle.shape('turtle')
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()
blue_turtle.speed('slow')
"""
# ----------------

# Turtle 2 - pink
pink_turtle = draw_turtle(t_name='pink_turtle', t_color='magenta',t_y=50)
"""
pink_turtle = Turtle()
pink_turtle.color('magenta')
pink_turtle.shape('turtle')
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()
pink_turtle.speed('slowest')
"""
# -------------------------------

# Turtle 3 - yellow
yellow_turtle = draw_turtle(t_name='yellow_turtle', t_color='yellow',t_y=-50)
"""
yellow_turtle = Turtle()
yellow_turtle.color('yellow')
yellow_turtle.shape('turtle')
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()
yellow_turtle.speed('slowest')
"""
# -------------------------------

# Turtle 4 - green
green_turtle = draw_turtle(t_name='green_turtle', t_color='green', t_y=-150)
"""
green_turtle = Turtle()
green_turtle.color('green')
green_turtle.shape('turtle')
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300, -150)
green_turtle.pendown()
green_turtle.speed('slowest')
"""

# pause for 1 second before start the race :
time.sleep(1)

# Move the turtles
my_screen.listen()
my_screen.onkey(move_func, "Right")

while True:
    blue_turtle.forward(random.randint(1, 10))
    pink_turtle.forward(random.randint(1, 10))
    yellow_turtle.forward(random.randint(1, 10))
#    green_turtle.forward(random.randint(1, 10))
    if blue_turtle.xcor() > 230:
        winner = blue_turtle
        break
    elif pink_turtle.xcor() > 230:
        winner = pink_turtle
        break
    elif yellow_turtle.xcor() > 230:
        winner = yellow_turtle
        break
    elif green_turtle.xcor() > 230:
        winner = green_turtle
        break

"""
while blue_turtle.xcor() <= 230 \
        and pink_turtle.xcor() <= 230 \
        and yellow_turtle.xcor() <= 230\
        and green_turtle.xcor() <= 230:
    blue_turtle.forward(random.randint(1, 10))
    pink_turtle.forward(random.randint(1, 10))
    yellow_turtle.forward(random.randint(1, 10))
#    green_turtle.forward(random.randint(1, 10))
"""

# print(winner.color())
# Celebrate the winner
game_end = True
winner.shapesize(2.5)
for i in range(1000):
    winner.right(5)
"""
if blue_turtle.xcor() > pink_turtle.xcor() \
        and blue_turtle.xcor() > yellow_turtle.xcor() \
        and blue_turtle.xcor() > green_turtle.xcor():
    print('Blue turtle wins')
    for i in range(1000):
        blue_turtle.right(5)
        blue_turtle.shapesize(2.5)
elif pink_turtle.xcor() > blue_turtle.xcor() \
        and pink_turtle.xcor() > yellow_turtle.xcor() \
        and pink_turtle.xcor() > green_turtle.xcor():
    print('pink turtle wins')
    for i in range(1000):
        pink_turtle.right(5)
        pink_turtle.shapesize(2.5)
elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor():
    print('yellow turtle wins')
    for i in range(1000):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(2.5)
else:
    print('green turtle wins')
    for i in range(1000):
        green_turtle.right(5)
        green_turtle.shapesize(2.5)
"""

my_screen.exitonclick()
