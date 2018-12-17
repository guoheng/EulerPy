
#The first two consecutive numbers to have two distinct prime factors are:
#
#14 = 2 x 7
#15 = 3 x 5
#
#The first three consecutive numbers to have three distinct prime factors are:
#
#644 = 2^2 x 7 x 23
#645 = 3 x 5 x 43
#646 = 2 x 17 x 19.
#
#Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

import logging
from prime import PrimeNumberPool

def defactor(n, prime):
    f = set()
    if (prime.IsPrime(n)):
        return f
    for p in prime.numbers:
        if (p >n):
            return f
        while (n % p == 0):
            f.add(p)
            n = n//p
    if (n>1):
        f.add(n)
    return f

def main(args):
    if args.test:
        n = 100
    else:
        n = 647

    prime = PrimeNumberPool()

    while (len(defactor(n, prime)) < 4 or len(defactor(n+1, prime)) < 4 or 
        len(defactor(n+2, prime)) < 4 or len(defactor(n+3, prime)) < 4):
        n += 1

    logging.info(n)
   
