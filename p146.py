# Investigating a Prime Pattern
# Problem 146
#
# The smallest positive integer n for which the numbers 
# n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. 
# The sum of all such integers n below one-million is 1242490.

# What is the sum of all such integers n below 150 million?

from prime import PrimeNumberPool
primes = PrimeNumberPool(load_from="data/prime_numbers.txt")

import logging
import time
logger = logging.getLogger('p146')


# Analysis
# let p = n^2+1
# p, p_2, p+6, p+8, p+12, p+26 are all primes,
# then p = 11 or p = 101 mod 210
# thus n = 210k + (10, 80, 130, 200)

#   Let n = qx + r where q is prime.
#   Then n^2 + s = q^2 x + 2qrx + (r^2 + s).
#   If q | (r^2 + s), then q | (n^2 + s).
#   So we do not want those n that satisfy q | ((n%q)^2 + s)
#   for some prime q and some s in {1, 3, 7, 9, 13, 27}.
def filter_on_prime(n, ps, cs):
    for p in ps:
        r = n % p
        r2 = r*r
        for c in cs:
            if (r2 + c) % p == 0:
                return True
    return False

def divisible(n, ps):
    # return true if n is divisible by any number is ps
    for p in ps:
        if n % p == 0:
            return True
    return False

def main(args):

    K = 1000
    M = K*K
    # constant offset
    cs = [1,3,7,9,13,27]
    
    if args.test:
        N = M
        ps = [2,3,5,7,11,13]
        candidates = [10]
        iter_b = 10
        pfilter = primes.numbers[:1000]
    else:
        N = 150*M
        ps = [2,3,5,7,11,13,17]
        candidates = [10,315410,927070]
        iter_b = 3
        pfilter = primes.numbers[:10000]

    pp = 1
    for p in ps:
        pp *= p

    pr = []
    for i in range(0, pp, 2):
        ipass = True
        for c in cs:
            n = i+c
            if divisible(n, ps):
                ipass = False
                break
        if ipass:
            pr.append(i)
    if args.verbosity > 2:
        logger.debug(pr)
    nr = []
    for i in range(pp):
        i2 = i*i%pp
        if i2 in pr:
            nr.append(i)
    if args.verbosity > 2:
        logger.debug(nr)

    logger.debug("run {} iterations, {} tests per iter, total {} tests".format(N//pp+1, len(nr), (N//pp+1)*len(nr)))
    ts2 = time.time()

    for i in range(iter_b, N//pp+1):
        #ipf = primes.getPrimeFactor(i)
        ts1 = ts2
        for r in nr:
            n = i*pp+r
            if n > N:
                break
            if filter_on_prime(n, pfilter, cs):
                continue

            n2 = n*n
            probably_prime = True
            for c in cs:
                p = n2 + c
                if not primes.IsPrime(p):
                    probably_prime = False
                    break
            if probably_prime:
                candidates.append(n)
                logger.debug("n={}, {}".format(n, [n2+x for x in cs]))

        ts2 = time.time()
        logger.debug("iteration {} took {}s".format(i+1, ts2-ts1))

    logger.debug(candidates)
    # double check the candidates
    result = []
    for n in candidates:
        n2 = n*n
        checked = True
        for c in range(1, 29, 2):
            p = n2 + c
            if c in cs:
                if not primes.IsPrime(p):
                    checked = False
                    break
            else:
                if primes.IsPrime(p):
                    checked = False
                    break
        if checked:
            result.append(n)
    logger.debug("check took {}s".format(time.time()-ts2))
    logger.debug(result)

    answer = sum(result)
    logger.info("answer: {}".format(answer))
