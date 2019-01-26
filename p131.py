
# Prime cube partnership
# Problem 131 
# There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + n^2p is a perfect cube.

# For example, when p = 19, 8^3 + 8^2×19 = 12^3.

# What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

# How many primes below one million have this remarkable property?

from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p131')
import time

# Analysis:
# n^3 + n^2p = m^3
# the only possible soltion is
# n = k^3, m = k^2(k+1), hence p = 3*k^2+3*k+1

def main(args):

    if args.test:
        K = 20
        N = 100
    else:
        K = 1000
        N = K*K

    primes = PrimeNumberPool(K)

    prime_cube_partnership = []
    for k in range(1, K):
        p = 3*k*(k+1)+1
        if primes.IsPrime(p):
            prime_cube_partnership.append(p)
            n = k*k*k
            m = k*k*(k+1)
            logger.debug("{}^3+{}^2x{} = {}^3".format(n, n, p, m))
        if p > N:
            break

    logger.debug(prime_cube_partnership)

    answer = len(prime_cube_partnership)
    logger.info("answer: {}".format(answer))
