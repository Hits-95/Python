# import Turtle package...
import turtle
import time

# create turtle scrn object...
sc = turtle.Screen()

# create turtle object pen...
pen = turtle.Turtle()

# define a def from a semi circle with dynamic radius or color...


def semi_circle(col, rad, val):

    # set the fill color of semi_circle..
    pen.color(col)
    # draw a circle...
    pen.circle(rad, -180)
    # move turtle to air...
    pen.up()
    # move the turtle to the given position ....
    pen.setpos(val, 0)
    # move the turtle to groun....
    pen.down()
    pen.right(180)


# set the color for draw...
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
# set the scrn feature...
sc.setup(600, 400)
# set the bg-scrn color
sc.bgcolor('black')
# set the turtle feature...
pen.right(90)
pen.width(5)
pen.speed(5)

# loop to draw 7 color...
for i in range(7):
    semi_circle(col[i], 10*(i+8), -10*(i+1))
