#

import os,logging
import time
import math

def main(args):
    description = '''
    Sum square difference
    Problem 6 
    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    '''

    if args.test:
        logging.info('Running test...')
        stop = 10+1
    else:
        stop = 100+1

    sum_squre = sum([i*i for i in range(1, stop)])
    square_sum = sum(list(range(1, stop)))**2

    solution = 'result:  {}'.format(square_sum - sum_squre)
    logging.info(solution)
