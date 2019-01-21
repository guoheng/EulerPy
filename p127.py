# abc-hits
# Problem 127 
# The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

# We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

# GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
# a < b
# a + b = c
# rad(abc) < c
# For example, (5, 27, 32) is an abc-hit, because:

# GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
# 5 < 27
# 5 + 27 = 32
# rad(4320) = 30 < 32
# It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

# Find ∑c for c < 120000.

import time
from util import gcd
from prime import PrimeNumberPool
import numpy as np
import logging
logger = logging.getLogger('p127')

primes = PrimeNumberPool()

def rad(a):
    return np.product(primes.getPrimeFactor(a))

def abc_hit(a,b):
    if a >= b:
        return False
    c = a+b
    if gcd(a,b) > 1:
        return False
    myrad = rad(a*b*c)
    return myrad < c

def find_max_power(c, ps):
    # input:
    #   c: max number
    #   ps: primes list
    # output:
    #   powers: list of max power for each primes
    powers = [1]*len(ps)
    myrad = np.product(ps)
    for i in range(len(ps)):
        a = myrad
        while a < c:
            a *= ps[i]
            powers[i] += 1
    return powers

def main(args):
    if args.test:
        C = 1000
        logger.debug("(5, 27, 32): {}".format(abc_hit(5,27)))
    else:
        C = 120000
        primes.FillTo(1200)
    
    abc_hits = []

    # Analysis:
    # for a abc-hit, rad(abc) = rad(a)*rad(b)*rad(c)
    # if a = 1, then rad(c-1)*rad(c) < c
    ts1 = time.time()
    for c in range(3, C):
        fc = primes.getPrimeFactor(c)
        pc  = np.product(fc)
        if pc == c:
            continue
        # check a = 1
        pb = rad(c-1)
        if pb*pc < c:
            logger.debug((1,c-1,c))
            abc_hits.append([1, c-1, c])
    ts2 = time.time()
    logger.debug("time for (1,b,c): {}".format(ts2-ts1))

    # for a > 1:
    candidate_c = []
    for c in range(3, C):
        pc = primes.getPrimeFactor(c)
        rad_c  = np.product(pc)
        pab = []
        for p in primes.numbers:
            if p not in pc:
                pab.append(p)
            if len(pab) == 2:
                break
        if rad_c*pab[0]*pab[1] > c:
            continue
        candidate_c.append({"number":c, "factor":pc, "rad":rad_c})
    ts3 = time.time()
    logger.debug("number of candidate_c: {}".format(len(candidate_c)))
    logger.debug("time for build candidate_c: {}".format(ts3-ts2))

    # a has 1 prime factor
    for cc in candidate_c:
        c = cc['number']
        rad_c = cc['rad']

        for p in primes.numbers:
            if p in cc['factor']:
                continue
            if p*rad_c > c//2:
                break
            a = p
            while a < c//2:
                b = c - a
                pb = primes.getPrimeFactor(b)
                rad_b = np.product(pb)
                if p*rad_b*rad_c < c:
                    logger.debug((a,b,c))
                    abc_hits.append([a, b, c])
                a *= p
    ts4 = time.time()
    logger.debug("a has 1 prime factor: {}".format(ts4-ts3))

    # a has 2 prime factor
    # refine candidates
    candidate_c2 = []
    for cc in candidate_c:
        rad_c = cc['rad']
        pab = []
        for p in primes.numbers:
            if p not in pc:
                pab.append(p)
            if len(pab) == 3:
                break
        if rad_c*pab[0]*pab[1]*pab[2] > cc['number']:
            continue
        candidate_c2.append(cc)
    logger.debug("refine number of candidate: {}".format(len(candidate_c2)))

    for cc in candidate_c2:
        c = cc['number']
        rad_c = cc['rad']
        for p1 in primes.numbers:
            if p1 in cc['factor']:
                continue
            if p1*p1*rad_c > c//2:
                break
            for p2 in primes.numbers:
                if p2 <= p1:
                    continue
                if p2 in cc['factor']:
                    continue
                rad_a = p1*p2
                if rad_a*rad_c > c//2:
                    break
                # find out the max power of p1/p2
                m1, m2 = find_max_power(c//2, [p1, p2])
                a1 = 1
                for i in range(m1):
                    a1 *= p1
                    a = a1
                    for j in range(m2):
                        a *= p2
                        if a > c//2:
                            break
                        b = c-a
                        rad_b = rad(b)
                        if rad_a*rad_b*rad_c < c:
                            logger.debug((a,b,c))
                            abc_hits.append([a, b, c])
    ts5 = time.time()
    logger.debug("a has 2 prime factor: {}".format(ts5-ts4))

    # refine candidates
    candidate_c3 = []
    for cc in candidate_c2:
        rad_c = cc['rad']
        pab = []
        for p in primes.numbers:
            if p not in pc:
                pab.append(p)
            if len(pab) == 4:
                break
        if rad_c*pab[0]*pab[1]*pab[2]*pab[3] > cc['number']:
            continue
        candidate_c3.append(cc)
    logger.debug("refine number of candidate: {}".format(len(candidate_c3)))

    # a has 3 prime factor
    for cc in candidate_c3:
        c = cc['number']
        rad_c = cc['rad']
        for p1 in primes.numbers:
            if p1 in cc['factor']:
                continue
            if p1*p1*p1*rad_c > c//2:
                break
            for p2 in primes.numbers:
                if p2 <= p1:
                    continue
                if p2 in cc['factor']:
                    continue
                if p1*p2*p2*rad_c > c//2:
                    break
                for p3 in primes.numbers:
                    if p3 <= p2:
                        continue
                    if p3 in cc['factor']:
                        continue
                    rad_a = p1*p2*p3
                    if rad_a*rad_c > c//2:
                        break
                    # find out the max power of p1/p2/p3
                    m1, m2, m3 = find_max_power(c//2, [p1, p2, p3])
                    a1 = 1
                    for i in range(m1):
                        a1 *= p1
                        a2 = a1
                        for j in range(m2):
                            a2 *= p2
                            if a2 > c//2:
                                break
                            a = a2
                            for k in range(m3):
                                a *= p3
                                b = c-a
                                if b < a:
                                    break
                                assert(b>a)
                                rad_b = rad(b)
                                if rad_a*rad_b*rad_c < c:
                                    logger.debug((a,b,c))
                                    abc_hits.append([a, b, c])
    ts6 = time.time()
    logger.debug("a has 3 prime factor: {}".format(ts6-ts5))


    logger.debug("There are {} abc-hit".format(len(abc_hits)))
    answer = sum([x[2] for x in abc_hits])
    logger.info("answer: {}".format(answer))
