import turtle
# let's get a nice setup
turtle.bgcolor("black") # background colour
turtle.pensize(5)
turtle.color("yellow")
turtle.speed(0)

# draw a square


# turtle.forward(80)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(90)
# turtle.forward(80)
#  turtle.left(90)
# turtle.forward(80)
# turtle.done()
for i in range(6):
 for colours in ["red", "yellow", "green", "orange", "purple", "white"]:
    turtle.color(colours)
    turtle.circle(150)
    turtle.left(10)
turtle.done()