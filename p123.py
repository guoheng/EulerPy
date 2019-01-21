# -*- coding: UTF-8 -*-

#Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.
#
#For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.
#
#The least value of n for which the remainder first exceeds 109 is 7037.
#
#Find the least value of n for which the remainder first exceeds 1010.

from prime import PrimeNumberPool
import time
import logging
logger = logging.getLogger('p123')


def main(args):

    t = [1]
    for i in range(10):
        t.append(t[-1]*10)

    prime = PrimeNumberPool()

    ts1 = time.time()
    if args.test:
        max_r = t[9]
        for i in range(t[4]*1):
            prime.NewPrime()
    else:
        max_r = t[10]
        for i in range(t[4]*3):
            prime.NewPrime()
    ts2 = time.time()
    logger.debug("prepare primes takes {}s".format(ts2-ts1))

    for i in range(len(prime.numbers)):
        if (i%2==1): continue
        p2 = prime.numbers[i]*prime.numbers[i]
        remainder = 2*(i+1)*prime.numbers[i] % p2
        if (remainder > max_r):
            logger.debug((i+1, prime.numbers[i], remainder))
            break

    answer = i+1
    logger.info("answer: {}".format(answer))

