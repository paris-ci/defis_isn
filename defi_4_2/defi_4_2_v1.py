# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author:  Arthur JOVART
# E-mail:  jovart.arthur@gmail.com
# Name:    defi 4.2
# Purpose: Trace un joli cube
# Created: 17/11/2015
# Python:  3.5
# Modules: builtins
# Licence: WTFPL (naméoh et oui elle existe)
# Notes : http://stackoverflow.com/a/9225336/3738545
# -------------------------------------------------------------------------------


import turtle
import random
cub = turtle.Turtle()

try:
    r = int(input("Entrez la quantitée de rouge (en %)  >"))
except ValueError:
    r = random.randrange(0,100)
    pass

try:
    v = int(input("Entrez la quantitée de vert (en %)   >"))
except ValueError:
    v = random.randrange(0,100)
    pass

try:
    b = int(input("Entrez la quantitée de bleu (en %)   >"))
except ValueError:
    b = random.randrange(0,100)
    pass

r = float(r/100)
v = float(v/100)
b = float(b/100)

# taille
try:
    x = int(input("Entrez la taille du cube (en pixels) >"))
except ValueError:
    x = random.randrange(100,225)
    pass

print("Valeurs : R: " + str(r) + ", V: " + str(v) + ", B: " + str(b) + ", Taille : ", str(x))

def avance():
    cub.forward(x)

# droite
cub.color(r,v,b)
cub.begin_fill()
cub.left(45)
avance()
cub.right(135)
avance()
cub.right(45)
avance()
cub.right(135)
avance()
cub.end_fill()

r = float(r/2)
v = float(v/2)
b = float(b/2)

# gauche
cub.color(r,v,b)
cub.begin_fill()
cub.left(45)
avance()
cub.left(135)
avance()
cub.left(45)
avance()
cub.left(135)
avance()
cub.end_fill()

r = float(r/2)
v = float(v/2)
b = float(b/2)

# haut
cub.color(r,v,b)
cub.begin_fill()
cub.left(45)
avance()
cub.right(90)
avance()
cub.right(90)
avance()
cub.right(90)
avance()
cub.right(135)
avance()
cub.end_fill()

print("Ouais c'est plus stylé en perspective ;)")
print("Cliquez sur la fenetre pour quitter !")
turtle.exitonclick()