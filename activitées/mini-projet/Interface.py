# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- Interface
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import sys
import ModificationsV2
import AffichageV2
import lectureV2

def main():
    print("Bonjour ! Vous etes sur le programme de lecture d'image de la classe d'ISN du lycée Saint Nicolas.\n\n")
    print("""Vous souhaitez :
    [1] - Afficher une image
    [2] - Afficher une image convertie en nuances de Gris
    [3] - Afficher une image convertie en noir et blanc
    [4] - Afficher l'image en texte (avec les métadonnées)

    """)
    choix = input("Entrez le numero choisi >")
    try:
        choix = int(choix)
    except ValueError:
        print("La valeur choisie n'est PAS valide. Veuillez entrer un nombre")
        sys.exit(1)

    if choix == 1:
        file = input("Quelle image souhaitez vous lire ? (Au format unix : ./image1.pbm) >")
        AffichageV2.afficher(lectureV2.lire(file))
    elif choix == 2:
        file = input("Quelle image souhaitez vous lire ? (Au format unix : ./image1.pbm) >")
        AffichageV2.afficher(ModificationsV2.toGrayScale(lectureV2.lire(file)))
    elif choix == 3:
        file = input("Quelle image souhaitez vous lire ? (Au format unix : ./image1.pbm) >")
        AffichageV2.afficher(ModificationsV2.toBlackAndWhite(lectureV2.lire(file)))
    elif choix == 4:
        file = input("Quelle image souhaitez vous lire ? (Au format unix : ./image1.pbm) >")
        print(lectureV2.lire(file))
    else:
        print("La valeur choisie n'est PAS valide. Veuillez entrer un nombre correct")
        sys.exit(1)


if __name__ == '__main__':
    main()
