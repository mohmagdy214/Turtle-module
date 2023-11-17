import turtle

sun = turtle.Turtle()

sun.speed(10)
sun.color("red","yellow")
sun.begin_fill()

for i in range(80):
    sun.forward(200)
    sun.left(125)
    sun.forward(200)


sun.end_fill()
sun.hideturtle()

turtle.done()
