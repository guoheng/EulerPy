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

def AllPrimes(ns):
    for n in ns:
        if not primes.IsPrime(n):
            return False
    return True

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

    use_Miller_Rabin = False

    if use_Miller_Rabin:
        is_pseudo_prime = primes.Miller_Rabin
    else:
        is_pseudo_prime = primes.IsPrime
    
    if args.test:
        N = M
        ps = [2,3,5,7,11,13]
        candidates = [10]
        iter_b = 10
        """
        candidates = [
            10,315410,927070,2525870,8146100,16755190,39313460,
            97387280, 119571820, 121288430, 130116970,
            139985660, 144774340
        ]
        result = []
        for n in candidates:
            n2 = n*n
            check_prime = True
            for c in range(1, 29, 2):
                if c in cs:
                    assert(primes.IsPrime(n2+c))
                else:
                    if primes.IsPrime(n2+c):
                        check_prime = False
                        logger.debug("{}^2+{} is prime".format(n, c))
                        break
            if check_prime:
                result.append(n)
        logger.debug(result)
        logger.info("answer = {}".format(sum(result)))
        """
    else:
        N = 150*M
        ps = [2,3,5,7,11,13,17]
        candidates = [10,315410,927070]
        iter_b = 1
        
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
    ts1 = time.time()

    pre_filter = dict()
    for r in nr:
        r2 = r*r
        rs = [(r2+x)%pp for x in cs]
        pre_filter[r] = []
        for k in rs:
            pre_filter[r] += primes.getPrimeFactor(k)
    for k, v in pre_filter.items():
        pre_filter[k] = set(v)

    ts2 = time.time()
    logger.debug("setup pre filter {}".format(ts2-ts1))

    for i in range(iter_b, N//pp+1):
        ipf = primes.getPrimeFactor(i)
        ts1 = ts2
        for r in nr:
            skip_r = False
            for p in ipf:
                if p in pre_filter[r]:
                    skip_r = True
                    break
            if skip_r:
                if args.verbosity > 2:
                    logger.debug("skip {}".format(r))
                continue

            n = i*pp+r
            if n > N:
                break
            n2 = n*n
            probably_prime = True
            for c in cs:
                p = n2 + c
                if not is_pseudo_prime(p):
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

    logger.debug(result)
    answer = sum(result)
    logger.info("answer: {}".format(answer))
