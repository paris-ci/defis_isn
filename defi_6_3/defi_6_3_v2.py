# -*- coding:Utf-8 -*-
#!/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author:  Arthur JOVART
# E-mail:  jovart.arthur@gmail.com
# Name:    defi_6_3_v1
# Purpose: Trace une fractale cubique
# Created: 20/11/2015
# Python:  3.5
# Modules: turple, random, sys
# Licence: WTFPL (naméoh et oui elle existe)
# Notes : http://stackoverflow.com/a/9225336/3738545
# -------------------------------------------------------------------------------


import random
import turtle
import sys

listeAngles = [45,90,135,180,225,270,315,360]

coteLimite = 20
facteurDivision = 2
angleCarre = 90
vitesse = 0

figure = turtle.Turtle()

figure.shape("classic")
figure.speed(vitesse)

def cube(cote,figure):
    for i in range(0,4):
        figure.forward(cote)
        figure.left(angleCarre)

def demanderLongueur():
    try:
        cote = int(turtle.textinput("Longeurs","Entrez une longueur en px qui constitura la taille de votre carré, tapez q pour quitter"))
        return cote
    except ValueError:
        print("Vous n'avez pas entré un nombre. Je quitte.")
        turtle.bye()
        sys.exit()


while True:
    cote = demanderLongueur()
    while cote >= coteLimite:
        figure.left(random.choice(listeAngles))
        cube(cote, figure)
        cote = int(cote/facteurDivision)
