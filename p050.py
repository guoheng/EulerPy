
#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import logging
from prime import PrimeNumberPool

def ConsecutivePrime(n, prime, ml):
    p = []
    i = 0
    sp = 0
    while (i < len(prime.numbers) and prime.numbers[i] <= n):
        while (sp < n):
            p.append(prime.numbers[i])
            sp += prime.numbers[i]
            i += 1
        if (sp == n):
            return p
        else:
            if (len(p) < ml):
                return [n]
            sp -= p[0]
            p = p[1:]
    return p

def main(args):
    ml = 1
    mp = 2


    if args.test:
        m = 1000
    else:
        m = 1000000

    prime = PrimeNumberPool(m)

    logging.debug(len(prime.numbers))

    for i in range(len(prime.numbers)):
        p = prime.numbers[-i-1]
        cp = ConsecutivePrime(p, prime, ml)
        if (len(cp) > ml):
            ml = len(cp)
            mp = p
            logging.info((mp, ml))
 