# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- defi_8_2
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

def cesarC(mot, cle):
    enc = ""
    l=len(mot)
    mot=mot.replace(" ","")
    mot = mot.upper()

    for i in range(l):
        asc=ord(mot[i])
        mot=mot.replace(" ","")
        if asc>=65 or asc<=90:
            asc += cle
            if asc>91:
                asc -= 26
            if asc<65:
                asc += 26
        enc += chr(asc)

    return enc

def supprime_accent(chaine):
    """ supprime les accents du texte source """
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']

    for i in range(len(accent)):
        chaine = chaine.replace(accent[i], sans_accent[i])

    return chaine


def warppercesarC(mot, cle):
    mot = mot.lower()
    mot = supprime_accent(mot)
    mot = mot.upper()
    mots = mot.split(" ")
    final = ""
    for mot in mots:
        final += cesarC(mot, cle)

    print(final)

cle = int(input("Entrez la clé > "))
message = str(input("message >"))

warppercesarC(message, cle)
