import turtle

wn = turtle.Screen()
my_turtle= turtle.Turtle()
wn.setup(starty=0, startx=50)
wn.screensize(400, 400)
my_turtle.setheading(180)


def spiral(_len):
    if _len > 6:
        my_turtle.forward(_len)
        my_turtle.left(90)
        spiral(_len-2)


spiral(200)
turtle.done()
