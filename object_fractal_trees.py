import turtle
import math

ang=math.radians(float(input("Enter the branch angle: ")))
ratio=float(input("Enter the shrinking ratio: "))
level=int(input("Enter the amount of levels: "))


def draw_line(x1, y1, x2, y2):
    myTurtle.penup()
    myTurtle.goto(x1, y1)
    myTurtle.pendown()
    myTurtle.goto(x2, y2)
    myTurtle.penup()


def distance(x1, y1, x2, y2):
    return math.sqrt(pow((x1-x2), 2)+pow((y1-y2), 2))


class Branch:

    def __init__(self, _start_x, _start_y, _end_x, _end_y, _angle_r, _angle_l):
        self.start_x=_start_x
        self.start_y = _start_y
        self.end_x= _end_x
        self.end_y = _end_y
        self.spawn=None
        self.angle_r=_angle_r
        self.angle_l = _angle_l

    def dist(self):
        return distance(self.start_x, self.start_y, self.end_x, self.end_y)*ratio

    def draw(self):
        draw_line(self.start_x, self.start_y, self.end_x, self.end_y)

    def branch_right(self):
        return Branch(self.end_x, self.end_y,
                      self.end_x + self.dist() * math.cos(self.angle_r),
                      self.end_y + self.dist() * math.sin(self.angle_r),
                      self.angle_r-(math.radians(90)-ang), self.angle_l+(math.radians(90)-ang))

    def branch_left(self):
        return Branch(self.end_x, self.end_y,
                      self.end_x - self.dist() * math.cos(self.angle_l),
                      self.end_y + self.dist() * math.sin(self.angle_l),
                      self.angle_r+(math.radians(90)-ang), self.angle_l-(math.radians(90)-ang))


wn = turtle.Screen()
myTurtle= turtle.Turtle()
tree=[]


def setup():
    wn.setup(startx=0, starty=0)
    myTurtle.setheading(90)
    wn.screensize(400, 400)
    root = Branch(0, (-wn.canvheight+100), 0, -100, ang, ang)
    tree.append(root)


def add_branches():
    for item in tree[::-1]:
        if item.spawn is None:
            tree.append(item.branch_right())
            tree.append(item.branch_left())
            item.spawn=True


if __name__ == '__main__':
    myTurtle.speed(9)
    setup()
    print(len(tree))
    for i in range(level):
        add_branches()
    for branch in tree:
        branch.draw()
    turtle.done()

