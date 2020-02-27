import turtle
size = int(input("What size should the circle be? (1-20)"))


def drawCircle(t, sz):

    """Make turtle t draw a circle of radius sz."""
    for i in range(360):
        t.forward(sz)
        t.left(1)


wn = turtle.Screen()             # Set up the window
wn.bgcolor("white")


tess = turtle.Turtle()           # create tess
drawCircle(tess, size)

wn.exitonclick()
