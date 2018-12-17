#Euler published the remarkable quadratic formula:
#
#n^2 + n + 41
#
#It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
#Using computers, the incredible formula n^2 - 79n + 1601 was discovered, 
#which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
#
#Considering quadratics of the form:
#
#    n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import logging
from prime import PrimeNumberPool

def cprime(a, b, primes):
    cp = 0
    n = 0
    while (1):
        p = abs(n*n+a*n+b)
        if (primes.IsPrime(p)):
            cp += 1
            n += 1
        else:
            return cp

def main(args):
    prime = PrimeNumberPool()

    r = 1000
    for i in range(r):
        prime.NewPrime()

    pb = []
    for b in prime.numbers:
        if (b < r):
            pb.append(b)
            pb.append(-b)

    pb.sort()

    max_cp = 30
    ab = []

    for a in range(-r, r):
        for b in pb:
            cp = cprime(a,b, prime)
            if (cp > max_cp):
                max_cp = cp
                ab = [a,b]

    logging.info(ab)
    logging.info(ab[0]*ab[1])
