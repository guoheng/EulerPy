
# Large repunit factors
# Problem 132 
# A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

# For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

# Find the sum of the first forty prime factors of R(10^9).

import time
from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p132')

primes = PrimeNumberPool()

def A(n):
    m = 1
    k = 1
    mk = 1
    while m != 0:
        k += 1
        mk = mk*10%n
        m = (m+mk) % n
    return k

def main(args):

    if args.test:
        K = 10
        N = 10
        logger.debug(primes.Factorize(1111111111))
        logger.debug(primes.Factorize(10**10+1))
        ns = [11,41,101, 271,3541,9091,27961]
        for n in ns:
            logger.debug("A({})={}".format(n, A(n)))
        logger.debug(ns)
        logger.debug(Ab(ns))
        return 0
    else:
        K = 10**9
        N = 40

    ts1 = time.time()
    primes.FillTo(200000)
    ts2 = time.time()
    logger.debug("setup time:{}".format(ts2-ts1))
    pf = []
    i = 2
    while len(pf) < N:
        i += 1
        p = primes.numbers[i]
        ap = A(p)
        if K % ap == 0:
            pf.append(p)
            logger.debug("A({}) = {}".format(p, ap))

    logger.debug(pf)
    answer = sum(pf)
    logger.info("answer: {}".format(answer))
