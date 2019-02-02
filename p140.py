
# Modified Fibonacci golden nuggets
# Problem 140 
# https://projecteuler.net/problem=140
# 

from math import sqrt
import logging
logger = logging.getLogger('p140')

from prime import PrimeNumberPool

# Analysis
# problem can be reduced to find integer n such that
# (n+3)x^2+(n+1)x-n = 0 has rational solution
# so (n+1)^2 + 4n(n+3) is a square number
#

def IsSqrt(n):
    s = int(sqrt(n))
    return s*s == n

def main(args):

    if args.test:
        N = 18
    else:
        N = 30

    primes = PrimeNumberPool()

    golden_nuggets = []

    n = 1
    while len(golden_nuggets) < N:
        d = (n+1)*(n+1)+4*n*(n+3)
        if IsSqrt(d):
            golden_nuggets.append(n)
            logger.debug("n={}, m={}".format(n, int(sqrt(d))))
        n += 1

    logger.debug(golden_nuggets)

    answer = sum(golden_nuggets)
    logger.info("answer: {}".format(answer))
