# -*- coding: UTF-8 -*-

#It is possible to write ten as the sum of primes in exactly five different ways:
#
#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2
#
#What is the first value which can be written as the sum of primes in over five thousand different ways?

import logging

from util import *

def prime_sum(n, prime_numbers):
    if (n < 2): return 0
    prime_lt_n = []
    for p in prime_numbers:
        if (p > n) : break
        prime_lt_n.append(p)
    prime_lt_n.reverse()
    return find_sum(n, prime_lt_n)

def find_sum(n, a):
    if (n < a[-1]): return 0
    if (len(a) == 1):
        if (n % a[0] == 0): 
            return 1
        return 0
    b = a[1:]
    d = n//a[0]
    sum = 0
    for i in range(d+1):
        sum += find_sum(n-i*a[0], b)
    if (n % a[0] == 0): sum += 1
    return sum

def main(args):
    if args.test:
        L = 10+1
    else:
        L = 100

    prime = PrimeNumberPool(L)

    for n in range(L//2, L):
        ps = prime_sum(n, prime.numbers)
        logging.debug("{} {}".format(n, ps))
        if ps > 5000:
            logging.info("answer: {}".format(n))
            logging.debug(ps)
            return 0

