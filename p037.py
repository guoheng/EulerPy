#!/usr/bin/python

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import logging
from prime import PrimeNumberPool

def is_tr_prime(n, all_prime):
    r = 0
    t = 1
    while (n>0):
        r += (n%10)*t
        if (r not in all_prime):
            return 0
        t = t*10
        if (n not in all_prime):
            return 0
        n = n//10
    return 1

def main(args):
    prime = PrimeNumberPool()
    for i in range(80000):
        prime.NewPrime()

    all_prime = set(prime.numbers)

    truncatable_prime = []

    for p in all_prime:
        if (p < 11):
            continue
        if (is_tr_prime(p, all_prime)):
            truncatable_prime.append(p)

    logging.debug(truncatable_prime)
    logging.info(sum(truncatable_prime))
