#
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?

import logging
import permute
from prime import PrimeNumberPool


def check(d, prime):
    for j in d:
        d.append(d[0])
        d = d[1:]
        n = 0
        for i in d:
            n = n*10 + i
        if (prime.IsPrime(n) == 0):
            return 0
    return 1    

def main(args):
    primes = PrimeNumberPool()
    odds = [1,3,5,7,9]
    cir_prime = [2,3,5,7]

    for d1 in odds:
        for d2 in odds:
            if (check([d1,d2], primes)):
                cir_prime.append(d1*10+d2)

    for d1 in odds:
        for d2 in odds:
            for d3 in odds:
                if (check([d1,d2, d3], primes)):
                    cir_prime.append(d1*100+d2*10+d3)

    for d1 in odds:
        for d2 in odds:
            for d3 in odds:
                for d4 in odds:
                    if (check([d1,d2,d3,d4], primes)):
                        cir_prime.append(d1*1000+d2*100+d3*10+d4)

    for d1 in odds:
        for d2 in odds:
            for d3 in odds:
                for d4 in odds:
                    for d5 in odds:
                        if (check([d1,d2,d3,d4,d5], primes)):
                            cir_prime.append(d1*10000+d2*1000+d3*100+d4*10+d5)

    for d1 in odds:
        for d2 in odds:
            for d3 in odds:
                for d4 in odds:
                    for d5 in odds:
                        for d6 in odds:
                            if (check([d1,d2,d3,d4,d5,d6], primes)):
                                cir_prime.append(d1*100000+d2*10000+d3*1000+d4*100+d5*10+d6)

    logging.debug(cir_prime)
    logging.info(len(cir_prime))