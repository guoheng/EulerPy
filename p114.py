# -*- coding: UTF-8 -*-

#A row measuring seven units in length has red blocks with a minimum length of three units placed on it, 
#such that any two red blocks (which are allowed to be different lengths) are separated by at least one 
#black square. There are exactly seventeen ways of doing this.
#
#How many ways can a row measuring fifty units in length be filled?
#
#NOTE: Although the example above does not lend itself to the possibility, in general it is permitted 
#to mix block sizes. For example, on a row measuring eight units in length you could use 
#red (3), black (1), and red (4).

import logging
logger = logging.getLogger('p114')

W = {-1: 1, 0: 1, 1:1, 2:1}

def FillRow(n):
    if n < -1: return 0
    if n in W:
        return W[n]
    
    num_ways = 1 # all black
    for first_block in range(3, n+1):
        for i in range(n-first_block+1):
            num_ways += FillRow(n-i-first_block-1)
            
    W[n] = num_ways
    return num_ways

def F(n):
    if n < -1: return 0
    if n in W:
        return W[n]
    
    num_ways = 1 # all black
    for first_block in range(3, n+1):
        for i in range(n-first_block+1):
            num_ways += FillRow(n-i-first_block-1)
            
    return num_ways

def main(args):

    logger.debug(FillRow(50))
    logger.info("answer: {}".format(F(50)))
