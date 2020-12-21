""" Graphical exercises."""

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
