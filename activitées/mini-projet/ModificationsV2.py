# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- ModificationsV2
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import statistics
import numpy as np

def toGrayScale(image_dict):
    listpix = image_dict["img"]
    newlist = []
    for pixel in listpix:
        r, v, b = pixel
        moyenne = int(statistics.mean([int(r), int(v), int(b)]))
        newlist.append((moyenne, moyenne, moyenne))
    image_dict["img"] = newlist
    return image_dict


def toBlackAndWhite(image_dict):
    image_dict = toGrayScale(image_dict)
    listpix = image_dict["img"]
    newlist = []
    for pixel in listpix:
        r, v, b = pixel
        if r >= 127:
            newlist.append((255, 255, 255))
        else:
            newlist.append((0, 0, 0))
    image_dict["img"] = newlist
    return image_dict


def retourne180(image_dict):
    listpix = image_dict["img"]
    listpix.reverse()

    image_dict["img"] = listpix
    return image_dict



def retourne90(image_dict):

    col = image_dict["meta"]["col"]
    lig = image_dict["meta"]["lig"]


    listepix = image_dict["img"]
    matrice = []
    for i in range(lig):
        matrice.append([])
        for j in range(col):
            matrice[i].append(tuple(listepix.pop()))



    listepix = []
    i = 1
    while i <= col:
        j = 1

        while j <= lig:
            listepix.append(matrice[lig-j][i-1])
            j += 1

        i += 1

    dict = {"meta": {"col": lig, "lig": col}, "img": listepix}
    return dict

