import turtle

t = turtle.Turtle()
t.speed(0)

def floc(l):
    if l < 3:
        t.forward(l)
        return
    floc(l / 3)
    t.lt(60)
    floc(l / 3)
    t.rt(120)
    floc(l / 3)
    t.lt(60)
    floc(l / 3)


def flocon(l):
    for i in range(3):
        floc(l)
        t.rt(120)

n = input("Combien d'itérations ? >")

flocon(n)
turtle.exitonclick()