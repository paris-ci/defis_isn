# -*- coding:Utf-8 -*-
#!/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author : Arthur JOVART
# E-mail : jovart.arthur@gmail.com
# Name   : defi 5.3
# Purpose: Nature d'un triangle
#          entrée sur STDIN, sortie STDOUT
# Created: 19/11/2015
# Python : 3.5
# Modules: builtins
# Licence: WTFPL (naméoh et oui elle existe)
# Notes  : http://stackoverflow.com/a/9225336/3738545
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

def is_triangle(longueurs):
    """ Vérifie que la figure est un triangle. """
    return len(longueurs) == 3

def is_possible_triangle(longueurs):
    """ Vérifie que la figure est un triangle possible. """
    assert(is_triangle(longueurs))
    longueurs.sort()
    a, b, c = longueurs
    return c <= b + a

def is_isocele(longueurs):
    """ Teste si un triangle est isocèle. """
    assert(is_triangle(longueurs))
    a, b, c = longueurs
    return a == b or b == c or a == c

def is_equilateral(longueurs):
    """ Teste si un triangle est équilatéral. """
    assert(is_triangle(longueurs))
    a, b, c = longueurs
    return a == b == c

def is_rectangle(longueurs):
    """ Teste si un triangle est rectangle. """
    assert(is_triangle(longueurs))
    longueurs.sort()
    a, b, c = longueurs
    return c**2 == a**2 + b**2

def triangle(longueurs):
    toreply = ""
    inloop = False
    toreply += "La figure dont les cotés sont de longueurs {0}".format(longueurs) + "\n>>>"
    if is_triangle(longueurs):
        if is_possible_triangle(longueurs):
            toreply += "est un triangle"
        else:
            toreply += "n'est pas un triangle."
            print(toreply)
            return
    else:
        toreply += "n'est pas un triangle."
        print(toreply)
        return
    if is_equilateral(longueurs):
        toreply += " équilatéral"
        inloop = True
        equi = True

    if is_rectangle(longueurs):
        toreply += " rectangle"
        inloop = True
        rect = True

    if is_isocele(longueurs):
        if not equi and not rect:
            toreply += " isocèle"
            inloop = True

    if not inloop:
        toreply += " quelconque"

    print(toreply + ".")

longueurs = [float(input("Entrez la longueur du 1er coté >")), float(input("Entrez la longueur du 2eme coté >")), float(input("Entrez la longueur du 3eme coté >"))]
triangle(longueurs)