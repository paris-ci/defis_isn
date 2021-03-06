# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- defi_8_2
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"



def cesarC(message, shift):
    message = message.lower()
    secret = ""
    for c in message:
        if c.isalpha():
            num = ord(c)
            num += shift
            if num > ord("z"):     # wrap if necessary
                num -= 26
            elif num < ord("a"):
                num += 26
            secret += chr(num)
        else:
            # don't modify any non-letters in the message; just add them as-is
            secret += c
    return secret

def supprime_accent(chaine):
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']

    for i in range(len(accent)):
        chaine = chaine.replace(accent[i], sans_accent[i])

    return chaine


def warppercesarC(mot, cle):
    mot = mot.lower()
    mot = supprime_accent(mot)
    mots = mot.split(" ")
    final = ""
    for mot in mots:
        final += " " + cesarC(mot, - cle)

    return final

message = "BU KLZ ZLJYLAZ KB IVUOLBY LZA KL KLTHUKLY ILHBJVBW H ZVP-TLTL LA WLB HBE HBAYLZ."

nombre = 0
possible = ""
Bcle = 0
for i in range(1, 26):
    Npossible = warppercesarC(message, i)
    Nnombre = Npossible.count("e")
    if Nnombre > nombre:
        nombre = Nnombre
        possible = Npossible
        print("[...] nouvelle possibilitée choisie : " + possible + "(score :" + str(nombre) + ")")
        Bcle = i

print("Meilleur possible (" + str(Bcle) + ") : ")
print(possible)
print("Avec un score de " + str(nombre))
