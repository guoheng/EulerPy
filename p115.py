# -*- coding: UTF-8 -*-

#A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
#
#Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.
#
#For example, F(3, 29) = 673135 and F(3, 30) = 1089155.
#
#That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.
#
#In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.
#
#For m = 50, find the least value of n for which the fill-count function first exceeds one million.

import logging
logger = logging.getLogger('p115')

def F(m, n):
    if n < m: return 1
    if n == m: return 2
    
    num_ways = 1 # all black
    for first_block in range(m, n+1):
        for i in range(n-first_block+1):
            num_ways += F(m, n-i-first_block-1)
            
    return num_ways

def main(args):
    logger.debug(F(3, 29))
    logger.debug(F(3, 30))
    logger.debug(F(10, 56))
    logger.debug(F(10, 57))

    k = 1000
    m = k*k
    for n in range(160, 170):
        fill_count = F(50, n)
        logger.debug('F(50, %d) = %d' % (n, fill_count))
        if fill_count > m:
            break
    logger.info("answer: {}".format(n))
