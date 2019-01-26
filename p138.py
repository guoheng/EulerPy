
# Special isosceles triangles
# Problem 138 
# https://projecteuler.net/problem=138
# 

from math import sqrt
import logging
logger = logging.getLogger('p138')

# Analysis
# let h = m^2-n^2, b/2 = 2mn
# then m = sqrt(5n^2+-1)+2n
#

def IsSqrt(n):
    s = int(sqrt(n))
    return s*s == n

def main(args):

    if args.test:
        N = 2
    else:
        N = 12

    isosceles = []

    n = 1
    while len(isosceles) < N:
        for i in [-1, 1]:
            d = 5*n*n + i
            if IsSqrt(d):
                m = int(sqrt(d)) + 2*n
                b = 4*m*n
                h = m*m - n*n
                l = m*m + n*n
                isosceles.append([b,h,l])
        n += 1

    logger.debug(n)
    logger.debug(isosceles)

    answer = sum([x[2] for x in isosceles])
    logger.info("answer: {}".format(answer))
