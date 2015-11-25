# -*- coding:Utf-8 -*-
#!/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author:  Arthur JOVART
# E-mail:  jovart.arthur@gmail.com
# Name:    defi_6_2_v1
# Purpose: Jeu du plus ou moins
# Created: 20/11/2015
# Python:  3.5
# Modules: sys, random
# Licence: WTFPL (naméoh et oui elle existe)
# Notes : http://stackoverflow.com/a/9225336/3738545
# Let's play
# -------------------------------------------------------------------------------

import sys
import random

print("Bienvenue au jeu du plus ou moins !\n••••••••••••••••••••••••••••••••••••••••••••••••••")

while True:
    finished = False
    nbreTours = 0
    min = 0
    max = 100
    nombreVise = random.randrange(min, max)
    print("••• ••• Nouvelle partie ! ••• •••")
    while not finished:
        nbreTours += 1
        astuce = int((max-min)/2 + min)
        try:
            nombreEntre = int(input("Entrez un nombre compris entre " + str(min) + " et " + str(max) + " (astuce : " + str(astuce) +") >"))
        except:
            print("Au revoir ! (Juste pour te déprimer, le nombre recherché était : " + str(nombreVise) + ")" )
            sys.exit(0)

        if nombreVise > nombreEntre:
            print("C'est plus grand !")
            min = nombreEntre
        elif nombreVise < nombreEntre:
            print("C'est plus petit !")
            max = nombreEntre
        else:
            print("Exact! Le nombre à trouver était bien : " + str(nombreVise) + "! Tu l'as trouvé en " + str(nbreTours) + " tours.")
            finished = True
