# -*- coding: UTF-8 -*-

#Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.

import logging
logger = logging.getLogger('p117')

Ways = [0]*50
Ways[0] = 1

def Tile(r):
    if (r == 0):
        return 1
    if (r < 0):
        return 0
    if (Ways[r-1] > 0):
        return Ways[r-1]
    red = 0
    for i in range(r-1):
        red += Tile(r-i-2)
    green = 0
    for i in range(r-2):
        green += Tile(r-i-3)
    blue = 0
    for i in range(r-3):
        blue += Tile(r-i-4)
    way = red+green+blue+1
    Ways[r-1] = way
    return way

def main(args):
    logger.debug(Tile(5))
    logger.debug(Tile(15))
    logger.debug(Tile(25))
    logger.debug(Tile(49))
    logger.info("answer: {}".format(Tile(50)))
