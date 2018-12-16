#

import os,logging
import time
import math
from prime import PrimeNumberPool

def MirrorNumber(left, odd=False):
    '''
    Construct a palindrome number

    Parameter:
    left: the left part of the number
    odd: False if the palindrome number have odd number of digit
        True if the palindrome number have even number of digit
    '''
    digits = []
    l = left
    while l > 0:
        digits.append(l%10)
        l = l // 10
    if odd:
        digits.pop(0)
    for d in digits:
        left = left*10+d
    return left

def Factorize2(n, primes):
    '''
    Check if integer n is a product of two 2-digit numbers
    '''
    factors = primes.getPrimeFactor(n)
    max_f = max(factors)
    # step 10 to 99 with max_f as step
    for i in range(1, 99//max_f+1):
        if i*max_f < 10:
            continue
        if n % (i*max_f) == 0:
            factor2 = n//(i*max_f)
            if factor2 > 9 and factor2 < 100:
                return (i*max_f, factor2)
    return []

def Factorize3(n, primes):
    '''
    Check if integer n is a product of two 3-digit numbers
    '''
    factors = primes.getPrimeFactor(n)
    logging.debug('factorize {} to {}'.format(n, factors))
    max_f = max(factors)
    # step 100 to 999 with max_f as step
    for i in range(1, 999//max_f+1):
        if i*max_f < 100:
            continue
        if n % (i*max_f) == 0:
            factor2 = n//(i*max_f)
            if factor2 > 99 and factor2 < 1000:
                return (i*max_f, factor2)
    return []

def main(args):
    description = '''
    Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    '''

    # analysis:
    # product of two 3-digit numbers <= 999*999 = 998001
    # start from the lagest palindrome, and try to factorize to product of two 3-digit numbers
    #

    maxp = 999
    primes = PrimeNumberPool(maxp)

    if args.test:
        logging.info('Running test...')
        # construct palindromic number
        for a in range(9, 0, -1):
            p1  = 1001*a 
            for b in range(9, -1, -1):
                p2 = p1 + 110*b
                factor2 = Factorize2(p2, primes)
                if len(factor2) > 0:
                    solution = 'largest palindrome {} made from the product of  {}'.format(p2, factor2)
                    logging.info(solution)
                    exit(0)
    else:
        t1 = time.time()
        # construct palindromic number
        for left in range(999, 100, -1):
            p  = MirrorNumber(left)
            factor3 = Factorize3(p, primes)
            if len(factor3) > 0:
                solution = 'largest palindrome {} made from the product of  {}'.format(p, factor3)
                logging.info(solution)
                t2 = time.time()
                logging.info('run time {}'.format(t2-t1))
                exit(0)
