#

import os,logging
import time
import math
from prime import PrimeNumberPool

def main(args):
    description = '''
    Smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    '''

    maxp = 999
    primes = PrimeNumberPool(maxp)

    if args.test:
        logging.info('Running test...')
        stop = 10
    else:
        stop = 20

    result = 1
    for p in primes.numbers:
        if p > stop:
            break
        power_of_p = p
        while (power_of_p <= stop//p):
            power_of_p *= p
        result *= power_of_p
    solution = 'result:  {}'.format(result)
    logging.info(solution)
