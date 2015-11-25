# -*- coding:Utf-8 -*-
#!/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author:  Arthur jo***t
# E-mail:  jo***t.arthur@gmail.com
# Name:    defi_6_1_v1
# Purpose: Calcul des factorielles
# Created: 20/11/2015
# Python:  3.5
# Modules: builtins
# Licence: WTFPL (naméoh et oui elle existe)
# Notes : http://stackoverflow.com/a/9225336/3738545
# Pour les grands nombres, attention aux limites de récursion !
# -------------------------------------------------------------------------------


def factorielle(x):
    if x==0:
        return 1
    else :
        return x * factorielle(x-1)
print("La factorielle de votre nombre es : " + str(factorielle(int(input("Quel es le nombre dont vous souhaitez calculer la factorielle ?")))))