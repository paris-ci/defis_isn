import turtle

t = turtle.Turtle()
t.speed(0)

def floc(l):
    if l < 3:
        t.forward(l + 10)
        return
    floc(l / 2)
    t.lt(60)
    floc(l / 2)
    t.rt(120)
    floc(l / 2)
    t.lt(60)
    floc(l / 2)


def flocon(l):
    for i in range(3):
        floc(l)
        t.rt(120)

n = int(input("Combien d'itérations ? >"))

flocon(n)
turtle.exitonclick()