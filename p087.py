# -*- coding: UTF-8 -*-

#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#
#28 = 2^2 + 2^3 + 2^4
#33 = 3^2 + 2^3 + 2^4
#49 = 5^2 + 2^3 + 2^4
#47 = 2^2 + 3^3 + 2^4
#
#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

import logging
from prime import PrimeNumberPool

def main(args):
    if args.test:
        M = 50
    else:
        M = 50*1000*1000

    prime = PrimeNumberPool()
    prime.IsPrime(M)

    rslt = []

    for p1 in prime.numbers:
        n1 = p1*p1
        for p2 in prime.numbers:
            n2 = p2*p2*p2
            if (n2 > M):
                break
            for p3 in prime.numbers:
                n3 = p3*p3*p3*p3
                if (n3 > M): break
                n = n1+n2+n3
                if (n < M):
                    rslt.append((n, p1, p2, p3))

    logging.debug(len(rslt))
    ns = set([x[0] for x in rslt])
    logging.info("answer: {}".format(len(ns)))
