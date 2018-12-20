# https://projecteuler.net/problem=64
#

import logging
from math import sqrt

def NextTerm(n, sn, p):
    (a, b) = p
    c = int(b/(sn-a))
    b1 = (n - a*a)/b
    a1 = c*(n-a*a)/b - a
    return [c, (a1,b1)]

def SqrtFraction(n):
    sn = sqrt(n)
    sf = [int(sn)]
    if (n == sf[0]*sf[0]):
        return sf
    pattern = set()
    p = (sf[0], 1)
    while (not p in pattern):
        pattern.add(p)
        [c, p] = NextTerm(n, sn, p)
        sf.append(c)
    return sf

def main(args):
    no = 0
    for n in range(2,10000):
        if (len(SqrtFraction(n)) % 2 == 0):
            no += 1
    logging.info("answer: {}".format(no))

