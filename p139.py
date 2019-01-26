
# Pythagorean tiles
# Problem 139 
# https://projecteuler.net/problem=139
# 

from math import sqrt
import logging
logger = logging.getLogger('p139')
from util import GCD

# Analysis
# problem can be reduced to find Pythagorean triple (a,b,c) such that c = 0 mod (b-a)
# Let a = m^2-n^2; b = 2mn; c = m^2+n^2; c = k(b-a)
# then m^2+n^2 = k(2mn+n^2-m^2)
# m = n(sqrt(2k^2-1)+k)/(k+1)

def IsSqrt(n):
    s = int(sqrt(n))
    return s*s == n

def main(args):

    K = 1000
    M = K*K
    L = 100*M

    triangles = dict()

    for k in range(2, L//2):
        x = 2*k*k-1
        s = int(sqrt(x))
        if s*s == x:
            n = k - 1
            m = k + s
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            g = GCD(a,b)
            a, b, c = a//g, b//g, c//g
            if a > b:
                a, b = b, a
            key = "{}".format((a,b,c))
            triangles[key] = a+b+c
            # logger.debug("k={}, sqrt(2k^2-1)={}".format(k, s))

    logger.debug(triangles)

    answer = 0
    for k, v in triangles.items():
        answer += L // v

    logger.info("answer: {}".format(answer))
