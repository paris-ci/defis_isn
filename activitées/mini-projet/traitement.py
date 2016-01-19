# -*- coding:Utf-8 -*-
#-------------------------------------------------------------------------------
# Name:
# Purpose:
# Author:
# Created:
#-------------------------------------------------------------------------------

from support import *

# ------------------------------------------------------------------------------
# Variables pour les tests unitaires !! NE PAS MODIFIER CETTE PARTIE !!
# Matrice et méta-donnée d'un fichier test au format PBM
M1 = [[0, 1, 1],
      [0, 0, 1],
      [1, 0, 0]]
meta1 = ("Matrice1","P1", 3, 3)

# Matrice et méta-donnée d'un fichier test au format PGM
M2 = [[255,215,185,155,125],
      [183,153,123, 93, 63],
      [120, 90, 60, 30,  0]]
meta2 = ("Matrice2","P2", 5, 3)

# Matrice et méta-donnée d'un fichier test au format PPM
M3 = [[(255,255,255), (127,127,127), (  0,  0,  0)],
      [(255,  0,  0), (180,  0,  0), (105,  0,  0)],
      [(255,255,  0), (180,180,  0), (105,105,  0)],
      [(  0,255,  0), (  0,180,  0), (  0,105,  0)],
      [(  0,255,255), (  0,180,180), (  0,105,105)],
      [(  0,  0,255), (  0,  0,180), (  0,  0,105)]]
meta3 = ("Matrice3","P3", 3, 6)

# ------------------------------------------------------------------------------
# Fonction de traitement des matrices images !! A VOUS DE JOUER !!

def rotation90():
    pass

def sym_hor():
    pass

def sym_ver():
    pass

def conv_PBM():
    pass

def conv_PGM():
    pass


# Test unitaire
afficher(M1, meta1)
##affiche(rotation90(M1, meta1))