# -*- coding: UTF-8 -*-

#A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).
#
#If red tiles are chosen there are exactly seven ways this can be done.
#
#If green tiles are chosen there are three ways.
#
#And if blue tiles are chosen there are two ways.
#
#Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.
#
#How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

import logging
logger = logging.getLogger('p116')

Ways = [[[0 for n in range(25)] for t in range(3)] for r in range(50)]

def Tile(r, t, n):
    if (r < t*n):
        return 0
    if (Ways[r-1][t-2][n-1] > 0):
        return Ways[r-1][t-2][n-1]
    if n == 1:
        way = r-t+1
        Ways[r-1][t-2][n-1] = way
        return way
    way = 0
    for i in range(r-t):
        way += Tile(r-i-t, t, n-1)
        
    Ways[r-1][t-2][n-1] = way
    return way

def main(args):
    row = 50
    way = 0
    for t in range(2,5):
        for n in range(1, row//t+1):
            way += Tile(row, t, n)

    logger.info("answer: {}".format(way))
