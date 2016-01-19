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
