# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author : Arthur jo***t
# E-mail : jo***t.arthur@gmail.com
# Name   : defi 5.1
# Purpose: Verifie si une année es bissextile, en une ligne
#          entrée sur STDIN, sortie STDOUT
# Created: 17/11/2015
# Python : 3.5
# Modules: builtins
# Licence: WTFPL (naméoh et oui elle existe)
# Notes  : http://stackoverflow.com/a/9225336/3738545
#          Ci-git PEP8  ==> T
# -------------------------------------------------------------------------------

def leapyr(n):
    if n % 400 == 0:
        return "L'année est bissexile !"
    if n % 100 == 0:
        return "L'année n'est PAS bissexile !"
    if n % 4 == 0:
        return "L'année est bissexile !"
    else:
        return "L'année n'est PAS bissexile !"

print(leapyr(int(input("Choississez une année >"))))