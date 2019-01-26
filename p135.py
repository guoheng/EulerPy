
# Same differences
# Problem 135 
# Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, 
# for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

# 34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

# It turns out that n = 1155 is the least value which has exactly ten solutions.

# How many values of n less than one million have exactly ten distinct solutions?

# Analysis
# let x = y+d, z = y-d
# x^2 - y^2 - z^2 = y(4d-y) = n
# 

import time
import logging
logger = logging.getLogger('p135')

def main(args):

    if args.test:
        N = 10000
    else:
        K = 1000
        N = K*K

    solutions = dict()

    for y in range(1, N):
        for d in range(y//4+1, y):
            n = y*(4*d-y)
            if n >= N:
                break
            if n in solutions:
                solutions[n].append(dict(y=y, d=d))
            else:
                solutions[n] = [dict(y=y, d=d)]
    
    sol10 = []
    for k in sorted(list(solutions.keys())):
        v = solutions[k]
        if len(v) == 10:
            sol10.append(k)
            logger.debug("n={}".format(k))
            logger.debug(v)

    answer = len(sol10)
    logger.info("answer: {}".format(answer))
