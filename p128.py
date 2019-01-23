# Hexagonal tile differences
# Problem 128 
# https://projecteuler.net/problem=128

import time
import pprint
from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p128')

primes = PrimeNumberPool()

def get_neibour(n):
    if n == 1:
        return list(range(2,8))
    
    # the tile t is from 3t(t-1)+2 to 3t(t+1)+1
    t = 1
    te = 3*t*(t+1)+1
    while te < n:
        t += 1
        te = 3*t*(t+1)+1
    tb = 3*t*(t-1)+2
    tile = list(range(tb, te+1))
    if t == 1:
        inner_tile = [1]
    else:
        inner_tile = list(range(3*(t-1)*(t-2)+2, tb))
    
    outer_tile = list(range(te+1, 3*(t+1)*(t+2)+2))
    
    idx = n - tile[0]
    edge = idx // t
    pos = idx % t

    if pos == 0:
        # 3 from outer, 2 from tile, 1 from inner 
        o_idx = edge*(t+1)
        return [
            inner_tile[edge*(t-1)], 
            tile[(idx+1)%(t*6)], tile[idx-1],
            outer_tile[o_idx-1], outer_tile[o_idx], outer_tile[o_idx+1]
            ]
    else:
        # 2 outer, 2 tile, 2 inner
        o_idx = edge*(t+1)+pos
        i_idx = edge*(t-1)+pos-1
        return [
            inner_tile[i_idx], inner_tile[(i_idx+1)%((t-1)*6)], 
            tile[(idx+1)%(t*6)], tile[idx-1],
            outer_tile[o_idx], outer_tile[(o_idx+1)%((t+1)*6)]
        ]

def PD(n):
    neibour = get_neibour(n)
    mydiff = [abs(x-n) for x in neibour]
    pd = 0
    for b in mydiff:
        if primes.IsPrime(b):
            pd += 1
    return pd

def AllPrime(mylist):
    for n in mylist:
        if not primes.IsPrime(n):
            return False
    return True

def main(args):
    if args.test:
        N = 10
    else:
        N = 2000
    
    ts1 = time.time()
    primes.FillTo(N*100)
    ts2 = time.time()
    logger.debug("setup time {}".format(ts2-ts1))

    # Analysis:
    # the number on tile t can be expressed as
    # n = 3t(t-1)+2+i where i in range(0, 6t)
    # further analysis show that only i = 0 or 6t-1 could result PD = 3

    t = 1
    pd3 = [1,2]
    while len(pd3) <= N:
        t += 1
        tb = 3*t*(t-1)+2
        neibour_b = [6*t-1, 6*t+1, 12*t+5]
        if AllPrime(neibour_b):
            pd3.append(tb)
    
        te = 3*t*(t+1)+1
        neibour_e = [6*t-1, 6*t+5, 12*t-7]
        if AllPrime(neibour_e):
            pd3.append(te)

        """ Another way to do it:
        for n in [3*t*(t-1)+2, 3*t*(t+1)+1]:
            pd = PD(n)
            if pd == 3:
                pd3a.append(n)
                if args.verbosity > 2:
                    logger.debug(n)
                    logger.debug([abs(x-n) for x in get_neibour(n)])
        """

    logger.debug("tile: {}".format(t))
    logger.debug(pd3)

    answer = pd3[N-1]
    logger.info("answer: {}".format(answer))
