# Searching a triangular array for a sub-triangle having minimum-sum
# Problem 150
# https://projecteuler.net/problem=150

from copy import deepcopy
from pprint import pformat
import logging
logger = logging.getLogger('p150')

def LinearCongruentialGenerator():
    # t := 0 
    # for k = 1 up to k = 500500: 
    #   t := (615949*t + 797807) modulo 2^20
    #   sk := t−2^19

    power_2_19 = 1<<19
    power_2_20 = power_2_19<<1
    t = 0
    s = []
    for k in range(500500):
        t = (615949*t + 797807) % power_2_20
        s.append(t - power_2_19)
    # construct the triangle
    tri = []
    for i in range(1000):
        i_b = i*(i+1)//2    # begin index
        i_e = i_b+i+1       # end index
        tri.append(s[i_b:i_e])
    return tri

def min_subtri(T):
    min_start_here = deepcopy(T)
    tlen = len(T)
    for r in range(tlen):
        for c in range(r+1):
            sum_subtri = [T[r][c]]
            for t in range(tlen-r-1):
                sum_subtri.append(sum_subtri[-1]+sum(T[r+1+t][c:c+t+2]))
            min_start_here[r][c] = min(sum_subtri)
    return min_start_here

def main(args):
    N = 1000
    tri = LinearCongruentialGenerator()

    if args.test:
        logger.debug(pformat(tri[:5]))
        logger.debug(pformat(min_subtri(tri[:5])))
    else:
        min_start_here = min_subtri(tri)

    answer = min([min(x) for x in min_start_here])
    logger.info("answer: {}".format(answer))
