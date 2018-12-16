#

import os,logging
import time
import math
from prime import PrimeNumberPool

def main(args):
    description = '''
    Summation of primes
    Problem 10 
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

    '''


    if args.test:
        maxp = 10
    else:
        maxp = 2*1000*1000

    ts1 = time.time()
    primes = PrimeNumberPool(maxp)
    ts2 = time.time()
    logging.debug('time for build prime number pool: {}'.format(ts2-ts1))
    if primes.GetLargestPrime() > maxp:
        result = sum(primes.numbers[:-1])
    else:
        result = sum(primes.numbers)
    
    solution = 'result:  {}'.format(result)
    logging.info(solution)
