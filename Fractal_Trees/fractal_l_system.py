import turtle,random


class Rule:
    def __init__(self, _rule_a, _rule_b):
        self.rule_a=_rule_a
        self.rule_b=_rule_b


colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# axiom="F"
axiom="F"
rules=list()
# FF+[+F]-[-F++] other design with the same instructions
# rules.append(Rule("F","F[F]-F+F[--F]+F-F"))
rules.append(Rule("F", "FF+[+F-F-F]-[-F+F+F]"))
# rules.append(Rule("F", "F[+F][-F]"))
# rules.append(Rule("F", "FF+[+F]-[-F++]"))
wn = turtle.Screen()
myTurtle= turtle.Turtle()
positions=[]
angles=[]


def generate(sentence):
    next_sentence=""
    for s_char in sentence:
        found = None
        for rule in rules:
            if s_char == rule.rule_a:
                found=True
                next_sentence+=rule.rule_b
                break
        if found is None:
            next_sentence+=s_char
    return next_sentence


def setup():
    wn.setup(startx=0, starty=-300)
    myTurtle.setheading(90)   
    wn.screensize(400, 400)


def interpret_text(instruction_set, _length):
    angle=25
    myTurtle.up()
    myTurtle.setpos(0, -300)    
    myTurtle.down()
    for inst in instruction_set:
        if inst == "F":
            myTurtle.forward(_length)
        elif inst=="+":
            myTurtle.right(angle)
        elif inst=="-":
            myTurtle.right(-angle)
        elif inst=="[":
            positions.append(myTurtle.pos())
            angles.append(myTurtle.heading())
        elif inst == "]":
            myTurtle.up()
            myTurtle.setpos(positions.pop())
            myTurtle.seth(angles.pop())
            myTurtle.down()
        


if __name__ == '__main__':
    print(wn.screensize())
    setup()
    phrase=axiom
    length=180
    # myTurtle._tracer(0)
    myTurtle.speed(10)
    for i in range(6):
        print(phrase)
        interpret_text(phrase, length)
        phrase=generate(phrase)
        length*=0.5        
        # myTurtle.pencolor(random.choice(colors))
    # interpret_text(phrase,length)
    turtle.done()
