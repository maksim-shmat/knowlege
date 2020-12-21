""" Graphical exercises."""
"""
import turtle

# fivecorners of 72 degrees
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
#turtle.exitonclick()  click on screen with turtle or print quit() in terminal
# square
for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)

# multi fivecorners
for i in range(0, 10):
    turtle.right(36)
    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(72)

# 061 
# Draw a triangle.

import turtle
for i in range(0, 3):
    turtle.forward(100)
    turtle.left(120)
turtle.exitonclick()

# 062
# Draw a circle.

import turtle

for i in range(0, 360):
    turtle.forward(1)
    turtle.left(1)
turtle.exitonclick()
"""

# 063
# Draw three squares in a row with a gap between each. Fill them using three
# different colours.

import turtle

turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()
turtle.exitonclick()
