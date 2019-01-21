# -*- coding: UTF-8 -*-

#The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
#
#If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
#
#Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.
#
#If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p124')
import numpy as np

def main(args):
    prime = PrimeNumberPool()
    n = 100000
    rod = {}

    for k in range(1, n+1):
        f = prime.getPrimeFactor(k)
        p = np.product(f)
        if (p in rod):
            rod_p = rod[p]
            rod_p.append(k)
        else:
            rod[p] = [k]

    # assume rod's key is sorted
    e_n = []
    for k in sorted(list(rod.keys())):
        e_n += rod[k]

    logger.info("answer: {}".format(e_n[10000-1]))
