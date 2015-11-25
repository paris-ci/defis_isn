# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author : Arthur JOVART
# E-mail : jovart.arthur@gmail.com
# Name   : defi 5.2
# Purpose: Exercice de calcul mental, SMILE!!!!!!
#          entrée sur STDIN, sortie TKINTER
# Created: 18/11/2015
# Python : 3.5
# Modules: turtle, random
# Licence: WTFPL (naméoh et oui elle existe)
# Notes  : http://stackoverflow.com/a/9225336/3738545
# -------------------------------------------------------------------------------

import turtle, random
wn = turtle.Screen()
smiles = turtle.Turtle()
smiles.shape("circle")


def bravo():
    smiles.penup()
    smiles.goto(-75,150)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(75,150)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(0,0)
    smiles.pendown()
    smiles.circle(100,90)

    smiles.penup()
    smiles.setheading(180)
    smiles.goto(0,0)
    smiles.pendown()
    smiles.circle(-100,90)
    smiles.penup()
    smiles.goto(0,125)

def nul():
    smiles.penup()
    smiles.goto(-75,150)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(75,150)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(0,100)
    smiles.pendown()
    smiles.circle(-100,-90)

    smiles.penup()
    smiles.setheading(180)
    smiles.goto(0,100)
    smiles.pendown()
    smiles.circle(100,-90)
    smiles.penup()
    smiles.goto(0,125)

print("Un peu de maths...")
operation = random.randrange(1,3) # 1 add, 2 sous, 3 mult
nbre1 = random.randrange(0,100)
nbre2 = random.randrange(0,100)

if operation == 1:
    res = nbre1 + nbre2
    ans = input("Combien font " + str(nbre1) + "+" + str(nbre2) + " > ")
elif operation == 2:
    res = nbre1 - nbre2
    ans = input("Combien font " + str(nbre1) + "-" + str(nbre2) + " > ")
else:
    res = nbre1 * nbre2
    ans = input("Combien font " + str(nbre1) + "*" + str(nbre2)+ " > ")


if float(ans) == float(res):
    print("BRAVO !")
    bravo()
else:
    print("Nan nan nan ! Le résultat était : " + str(res))
    nul()


turtle.exitonclick()