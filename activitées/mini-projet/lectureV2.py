# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
defis -- lectureV2
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import os
from collections import deque

def _createMeta(img_list):
    # img_format = img_file[0] #P1
    col = int(img_list[1])
    lig = int(img_list[2])

    dict = {"meta": {"col": col, "lig": lig}, "img": []}
    return dict


## PBM ##

def _lirePBM(img_list):
    dict = _createMeta(img_list)

    for line in img_list[3:]:
        dict["img"] += line.split()

    return dict


def _PBMtoPPM(dict):
    newlist = []
    for item in dict["img"]:
        if item == "1":
            newlist.append((0, 0, 0))
        else:
            newlist.append((255, 255, 255))
    dict["img"] = newlist
    return dict


## PGM ##

def _lirePGM(img_list):
    dict = _createMeta(img_list)

    for line in img_list[4:]:
        dict["img"] += line.split()

    return dict

def _PGMtoPPM(dict):
    newlist = []
    for item in dict["img"]:
        newlist.append((item, item, item))

    dict["img"] = newlist
    return dict


## PPM ##

def _lirePPM(img_list):
    dict = _createMeta(img_list)
    listVal = []

    for line in img_list[4:]:
        listVal.extend(line.split())

    taille = len(listVal)
    listVal = deque(listVal)
    for numero in range(0, int(taille / 3)):
        turple = ((listVal.popleft()), (listVal.popleft()), (listVal.popleft()))

        dict["img"].append(turple)

    return dict


def lire(fichier):
    """

    :param fichier: Nom du fichier, avec l'extension.
    :return: Dict, dans ce genre : {"meta" : {"col" : 2, "lig" : 3}, "img" : [(255, 255, 255), (253, 0, 34), (233, 0, 0), (153, 232, 7), ...}
    """

    filename, file_extension = os.path.splitext(fichier)

    with open(fichier, 'r') as f:
        img_list = f.read().splitlines()

    if file_extension == ".pbm":
        image = _PBMtoPPM(_lirePBM(img_list))
    elif file_extension == ".pgm":
        image = _PGMtoPPM(_lirePGM(img_list))
    elif file_extension == ".ppm":
        image = _lirePPM(img_list)
    else:
        raise FileExistsError

    return image


