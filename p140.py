
# Modified Fibonacci golden nuggets
# Problem 140 
# https://projecteuler.net/problem=140
# 

from math import sqrt
import logging
logger = logging.getLogger('p140')

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
        N = 20
    else:
        N = 30

    golden_nuggets = []
    golden_m = []

    # n = 21k + 0,2,5
    k = 0
    while len(golden_nuggets) < N:
        for r in [0, 2, 5]:
            n = 21*k + r
            if n == 0:
                continue
            d = (n+1)*(n+1)+4*n*(n+3)
            m = int(sqrt(d))
            if m*m == d:
                golden_nuggets.append(n)
                golden_m.append(m)
                logger.debug("n={}, m={}, k={}".format(n, m, k))
                if len(golden_m) > 3:
                    k = int(golden_m[-4]*1.00045) - 1
                    logger.debug("jump k to {}".format(k))
        k += 1

    logger.debug(golden_nuggets)

    answer = sum(golden_nuggets)
    logger.info("answer: {}".format(answer))
