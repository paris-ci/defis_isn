# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# ------------------------------------------------------------------------------
# Author : Arthur JOVART
# E-mail : jovart.arthur@gmail.com
# Name   : defi 5.4
# Purpose: Verifie si une année es bissextile, en une ligne
#          entrée sur STDIN, sortie STDOUT
# Created: 17/11/2015
# Python : 3.5
# Modules: builtins
# Licence: WTFPL (naméoh et oui elle existe)
# Notes  : http://stackoverflow.com/a/9225336/3738545
#          Ci-git PEP8  ==> T
# -------------------------------------------------------------------------------

(lambda __g, __print: [(__print(leapyr(int(input('Choississez une année >')))), None)[1] for __g['leapyr'], leapyr.__name__ in [(lambda n: (lambda __l: [(lambda __after: "L'année est bissexile !" if ((__l['n'] % 400) == 0) else __after())(lambda: (lambda __after: "L'année n'est PAS bissexile !" if ((__l['n'] % 100) == 0) else __after())(lambda: (lambda __after: "L'année est bissexile !" if ((__l['n'] % 4) == 0) else "L'année n'est PAS bissexile !")(lambda: None))) for __l['n'] in [(n)]][0])({}), 'leapyr')]][0])(globals(), __import__('builtins').__dict__['print'])
