# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- AffichageV2
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import tkinter as Tk
from collections import deque

def afficher(image_dict):
    """ Affiche une image à  partir d'une matrice"""

    listPix = image_dict["img"]

    listPix = deque(listPix)

    col = image_dict["meta"]["col"]
    lig = image_dict["meta"]["lig"]

    t = 400//max(lig,col)

    fen = Tk.Tk()
    fen.title("Image " + str(col) + "x" + str(lig))
    can = Tk.Canvas(fen, width = col*t + 18, height = lig*t + 18, bg = 'white')
    can.pack(side = Tk.TOP, padx = 5, pady = 5)


    for y in range(lig) :
        for x in range(col) :
            r, v, b = listPix.popleft()
            color = '#%02x%02x%02x' % (int(r),int(v),int(b))
            can.create_rectangle(10+x*t, 10+y*t, 10+(x+1)*t, 10+(y+1)*t, outline = color, fill = color)

    fen.mainloop()

