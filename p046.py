#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
#9 = 7 + 2x1^2
#15 = 7 + 2x2^2
#21 = 3 + 2x3^2
#25 = 7 + 2x3^2
#27 = 19 + 2x2^2
#33 = 31 + 2x1^2
#
#It turns out that the conjecture was false.
#
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import logging
from prime import PrimeNumberPool

squares = [1, 4, 9]

def Check(n, prime):
    if prime.IsPrime(n):
        return 0
    while (squares[-1] < n//2):
        squares.append(len(squares)*len(squares))
        
    for sq in squares:
        if (sq*2 >= n):
            return 0
        if (prime.IsPrime(n-sq*2)):
            return 1

def main(args):
    prime = PrimeNumberPool()

    n = 33
    done = 0
    while (done == 0):
        if (prime.IsPrime(n)):
            n += 2
            continue
        if (Check(n, prime) == 0):
            logging.info(n)
            done = 1
        else:
            n += 2

