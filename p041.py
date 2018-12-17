
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?

import logging
from prime import PrimeNumberPool
import permute

def ispanprime(d, prime):
    mp = 0
    for p in permute.all_perms(d):
        n = 0
        for i in p:
            n = n*10 + i
        if (prime.IsPrime(n) and n > mp):
            mp = n
    return mp

def main(args):
    if args.test:
        n = 3
    else:
        n = 8

    prime = PrimeNumberPool()

    for i in range(2,n):
        logging.debug(ispanprime(list(range(1,i+1)), prime))
