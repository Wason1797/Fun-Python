import turtle

_angle=70


def tree(branchLen,t):
    if branchLen > 10:
        t.forward(branchLen)
        t.right(_angle)
        tree(branchLen*0.67,t)
        t.left(_angle*2)
        tree(branchLen*0.67,t)
        t.right(_angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
