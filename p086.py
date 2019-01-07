# -*- coding: UTF-8 -*-

#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
#
#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route is not always integer.
#
#By considering all cuboid rooms up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest distance is integer when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.
#
#Find the least value of M such that the number of solutions first exceeds one million.

import logging
from math import sqrt

pTriple = set()
def PythagoreanTriple(L):
    '''find primitive Pythagorean triples that the longest rightangle edge <=L'''
    M = int(sqrt(L))+1
    for n in range(1,M):
        for m in range(n+1, M+1):
            t = [m*m-n*n,2*m*n]
            t.sort()
            for i in range(1, L//t[1]):
                pTriple.add((t[0]*i, t[1]*i))

def NumMutate(a, b, c):
    return 1
    t = set([a, b, c])
    if (len(t) == 1): return 1
    if (len(t) == 2): return 3
    return 6

numSols = {}
def NumSols(m):
    if (m < 3): return 0
    if (m in numSols): return numSols[m]
    ns = 0
    for (a,b) in pTriple:
        if (b == m):
            ns += a//2
        if (a == m):
            if (b > m*2): continue
            ns += m-b//2
            if (b%2 == 0): ns += 1
    ns += NumSols(m-1)
    numSols[m] = ns
    return ns

def main(args):
    if args.test:
        M = 2000
        m = 90
    else:
        M = 1000000
        m = 1000

    PythagoreanTriple(10000)

    for n in range(99, 101):
        logging.debug("{} distinct cuboids for M={}".format(NumSols(n), n))

    while (NumSols(m) < M):
        m += 1
    logging.debug(NumSols(m))
    logging.info("answer: {}".format(m))
