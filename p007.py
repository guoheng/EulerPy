#

import os,logging
import time
import math
from prime import PrimeNumberPool

def main(args):
    description = '''
    10001st prime
    Problem 7 
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    '''

    primes = PrimeNumberPool()

    if args.test:
        logging.info('Running test...')
        idx = 6-1
    else:
        idx = 10001-1

    num_primes = primes.NumberOfPrimes()
    for i in range(idx+1-num_primes):
        primes.NewPrime()
    
    result = primes.numbers[idx]
    solution = 'result:  {}'.format(result)
    logging.info(solution)
