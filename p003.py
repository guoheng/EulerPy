#

import os,logging
import time
import math
from prime import PrimeNumberPool

def main(args):
    description = '''
    Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    '''

    if args.test:
        number = 13195
    else:
        number = 600851475143

    logging.debug('test with {}'.format(number))

    maxp = round(math.sqrt(number)) + 1
    ts1 = time.time()
    primes = PrimeNumberPool(maxp)
    ts2 = time.time()
    logging.debug('time for build prime number pool: {}'.format(ts2-ts1))
    factors = primes.getPrimeFactor(number)
    logging.debug('factors:{}'.format(factors))
    ts3 = time.time()
    logging.debug('time for factorize: {}'.format(ts3-ts2))
    solution = 'largest prime factor of the number {} is {}'.format(number, factors[-1])
    logging.info(solution)
