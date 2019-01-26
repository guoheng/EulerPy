
# Fibonacci golden nuggets
# Problem 137 
# https://projecteuler.net/problem=137
# 

from math import sqrt
import logging
logger = logging.getLogger('p137')

# Analysis
# problem can be reduced to find integer n such that
# nx^2+(n+1)x-n = 0 has rational solution
# so (n+1)^2 + (2n)^2 = m^2
# let n+1 = a^2 - b^2, 2n = 2ab
# That require 5b^2+4 be a square number
#

def IsSqrt(n):
    s = int(sqrt(n))
    return s*s == n

def main(args):

    if args.test:
        N = 10
    else:
        N = 15

    golden_nuggets = []

    b = 1
    while len(golden_nuggets) < N:
        d = 5*b*b+4
        if IsSqrt(d):
            c = int(sqrt(d)) - b
            if c % 2 == 0:
                a = b + c//2
                n = a*b
                golden_nuggets.append(n)
        b += 1

    logger.debug(b)
    logger.debug(golden_nuggets)

    answer = golden_nuggets[-1]
    logger.info("answer: {}".format(answer))
