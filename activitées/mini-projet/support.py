# -*- coding:Utf-8 -*-
#------------------------------------------------------------------------------
# Author:  M. SALVA
# Name:    systeme.py
# Purpose: Affichage d'une image au format PBM, PGM ou PPM
# Created: 29/12/2015
# Python:  3.2
# Modules: tkinter
# Licence: Creative Commons BY NC SA
#-------------------------------------------------------------------------------

from tkinter import *


# ------------------------------------------------------------------------------
# Fonction d'ouverture du fichier

def lire_matrice(fichier, Nbligne):
    """ Lis la matrice et renvoi une liste de valeur str."""
    N = ""
    for i in range(Nbligne):
        ligne = fichier.readline()
        ligne = ligne.replace("\n"," ")
        for i in range(4):
            ligne = ligne.replace("  "," ")
        N = N + ligne
    N = N.strip().split(" ")
    return N

def ouvrir(nom):
    """
    Ouvre un fichier PBM, PGM ou PPM et le converti en matrice.
    Le premier élément est le format,
    Le deuxième le nombre de colonne,
    Le troisième le nombre de ligne,
    Le reste, la matrice.
    """

    nom=nom.split(".")[0]
    try :
        f = open(nom + ".pbm",'r')
    except :
        try :
            f = open(nom + ".pgm",'r')
        except :
            try :
                f = open(nom + ".ppm",'r')
            except :
                raise FileNotFoundError("Il n'existe pas de fichier : " + nom)

    # -------------------------
    # Conversion de la matrice
    img_format = f.readline()[:2]
    col = int(f.readline()[:3])
    lig = int(f.readline()[:3])
    meta_donnee = (nom, img_format, col, lig)

    if img_format !="P1":
        ech = int(f.readline()[:3])

    N = lire_matrice(f,lig)

    M = []
    for y in range(lig):
        M.append([])
        for x in range(col):
            if img_format == "P1":
                try :
                    M[y].append(int(N[x+y*col]))
                except:
                    M[y].append(1)

            elif img_format == "P2":

                try :
                    M[y].append(int(N[x+y*col]))
                except:
                    M[y].append(0)

            elif img_format == "P3":
                try :
                    i = y*(col*3)+x*3
                    M[y].append((int(N[i+0]),int(N[i+1]),int(N[i+2])))
                except:
                    M[y].append((0,0,0))

    f.close()

    return M, meta_donnee

# ------------------------------------------------------------------------------
# Affichage de l'image

def afficher(matrice=None, meta_donnee=None, size=400, fichier=False):
    """ Affiche une image à  partir d'une matrice"""

    if fichier: # Ouverture du fichier et affichage
        matrice, meta_donnee = ouvrir(fichier)


    titre, img_format, col, lig = meta_donnee

    t = (size-20)//max(col,lig) #Pour avoir toujour un affichage de 800 pixel

    fen = Tk()
    fen.title(titre+".%s %sx%s"% ({"P1":"pbm","P2":"pgm","P3":"ppm"}[img_format], col, lig))
    can = Canvas(fen, width = col*t + 18, height = lig*t + 18, bg = 'white')
    can.pack(side = TOP, padx = 5, pady = 5)

    if img_format == "P1":
        for x in range(col) :
            for y in range(lig) :
                if matrice[y][x] == 1 :
                    color = "black"
                    can.create_rectangle(10+x*t, 10+y*t, 10+(x+1)*t, 10+(y+1)*t, outline = color, fill = color)

    elif img_format == "P2":
        for x in range(col) :
            for y in range(lig) :
                r, v, b = matrice[y][x], matrice[y][x], matrice[y][x]
                color = '#{:02x}{:02x}{:02x}'.format(r,v,b)
                can.create_rectangle(10+x*t, 10+y*t, 10+(x+1)*t, 10+(y+1)*t, outline = color, fill = color)

    elif img_format == "P3":
        for x in range(col) :
            for y in range(lig) :
                r, v, b = matrice[y][x]
                color = '#{:02x}{:02x}{:02x}'.format(r,v,b)
                can.create_rectangle(10+x*t, 10+y*t, 10+(x+1)*t, 10+(y+1)*t, outline = color, fill = color)
    else:
        print("Le format d'image n'est pas supporté.")

    fen.mainloop()

# ------------------------------------------------------------------------------
# Sauvegarde de l'image

def sauver(M, meta_donnee):
    """ Sauvegarde l'image dans un fichier."""
    titre, img_format, col, lig = meta_donnee

    nom = titre + "_modifie." + {"P1":"pbm","P2":"pgm","P3":"ppm"}[img_format]
    fout = open(nom,'w')
    fout.write(img_format+'\n')
    fout.write(str(col)+'\n')
    fout.write(str(lig)+'\n')

    if img_format != "P1":
        fout.write('255\n')

    if img_format != "P3":
        for y in range(lig):
            t = ''
            for x in range(col):
                pix = str(M[y][x])
                if len(pix) == 1:
                    pix = "  " + pix
                elif len(pix) == 2:
                    pix= ' ' + pix

                t += pix + " "
            fout.write(t + '\n')
    else:
        for y in range(lig):
            t = ''
            for x in range(col):
                for i in range(3):
                    pix = str(M[y][x][i])
                    if len(pix) == 1:
                        pix = "  " + pix
                    elif len(pix) == 2:
                        pix= ' ' + pix
                    t += pix + " "
            fout.write(t + '\n')

    fout.close()

# ------------------------------------------------------------------------------
# Programme principal

##from traitement_solution import *

def main():
    M, meta = ouvrir("monty_python40")
    print(M)
##    M, meta = resize(M, meta)
    afficher(M, meta)
##    sauver(M, meta)

if __name__ == '__main__':
    main()

