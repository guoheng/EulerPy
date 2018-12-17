#!/usr/bin/python

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#
#It can be verified that the sum of both diagonals is 101.
#
#What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?

import logging

def main(args):

    n = (1001 - 1)//2

    s = 0
    for i in range(1,2*n+1):
        s += (2*i*i+i)

    s += 4*n*n+7*n+1

    logging.info(s)
