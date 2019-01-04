
#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
#If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
#By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

import logging
from math import ceil
from prime import PrimeNumberPool

def HCF(n, d, prime):
    for p in prime.getPrimeFactor(n):
        if (d % p == 0):
            return 0
    return 1

def main(args):
    if args.test:
        m = 10
    else:
        m = 1000*1000

    prime = PrimeNumberPool()

    md = 5
    mn = 2

    for d in range(2, m):
        if d == 7:
            continue
        n = d * 3 // 7
        if (n>mn*d/md and HCF(n, d, prime)):
            mn = n
            md = d
            logging.debug("{}/{}".format(mn, md))

    logging.info("answer: {}/{}".format(mn, md))
    logging.debug(prime.Factorize(mn))
    logging.debug(prime.getPrimeFactor(mn))
    logging.debug(prime.Factorize(md))
    logging.debug(prime.getPrimeFactor(md))
