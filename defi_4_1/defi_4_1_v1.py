# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author:  Arthur jo***t
# E-mail:  jo***t.arthur@gmail.com
# Name:    defi 4.1
# Purpose: Demande deux valeurs a et b en pixel et trace sous turtle le vecteur
#          AB de coordonnées (a,b).
# Created: 17/11/2015
# Python:  3.5
# Modules: builtins
# Licence: WTFPL (naméoh et oui elle existe)
# Notes : http://stackoverflow.com/a/9225336/3738545
# -------------------------------------------------------------------------------

from turtle import *
shape("turtle")
goto(float(input("Entrez x > ")), float(input("Entrez y > ")))
print("Cliquez sur la fenetre pour quitter !")
exitonclick()