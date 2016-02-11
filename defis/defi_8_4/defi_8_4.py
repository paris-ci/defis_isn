# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- defi_8_2
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


def supprime_accent(chaine):
    """ supprime les accents du texte source """
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', "-", "!", "."]
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a', "", "", ""]

    for i in range(len(accent)):
        chaine = chaine.replace(accent[i], sans_accent[i])

    return chaine


def cesarC(mot, cle):
    enc = ""
    l = len(mot)
    mot = mot.upper()

    for i in range(l):
        asc = ord(mot[i])
        if asc >= 65 or asc <= 90:
            asc += cle
            if asc > 90:
                asc -= 26
            if asc < 65:
                asc += 26
        enc += chr(asc)

    return enc


def warppercesarC(mot, cle):
    mot = mot.lower()
    mot = supprime_accent(mot)
    mot = mot.upper()
    mots = mot.split(" ")
    final = ""
    for mot in mots:
        final += " " + cesarC(mot, cle)

    return final


message = str(input("message >"))

nombre = 0
possible = ""
Bcle = 0
for i in range(1, 26):
    Npossible = warppercesarC(message, i)
    Nnombre = Npossible.count("E")
    if Nnombre > nombre:
        nombre = Nnombre
        possible = Npossible
        print("[...] nouvelle possibilitée choisie : " + possible + "(score :" + str(nombre) + ")")
        Bcle = i

print("Meilleur possible (" + str(Bcle) + ") : ")
print(possible)
print("Avec un score de " + str(nombre))
