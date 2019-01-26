
# Composites with prime repunit property
# Problem 130 
# A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

# Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

# You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

# However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

# Find the sum of the first twenty-five composite values of n for which
# GCD(n, 10) = 1 and n − 1 is divisible by A(n).

from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p130')

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
    primes = PrimeNumberPool()

    if args.test:
        N = 5
        for n in [7, 41]:
            logger.debug("A({}) = {}".format(n, A(n)))
    else:
        N = 25
    
    composite = []
    t = 1
    while len(composite) < N:
        t += 1
        for d in [1, 3, 7, 9]:
            n = t*10+d
            if primes.IsPrime(n):
                continue
            an = A(n)
            if (n-1) % an == 0:
                composite.append(n)
                logger.debug("A({}) = {}".format(n, an))
    
    logger.debug(composite)

    answer = sum(composite)
    logger.info("answer: {}".format(answer))
