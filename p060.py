
#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
import logging
from prime import PrimeNumberPool
import time

def CatNum(a,b):
    c = b
    while (c):
        c = c//10
        a = a*10
    return a+b


def Check(p, q, cprime):
    for a in q:
        if (not (a, p) in cprime):
            return 0
    return 1

def main(args):
    prime = PrimeNumberPool()

    cprime = set()

    ts1 = time.time()
    m = 2000
    for i in range(m):
        prime.NewPrime()

    pm = prime.numbers[:m]
    ts2 = time.time()
    logging.debug("time for build primes {}".format(ts2-ts1))

    for i in range(m):
        p1 = pm[i]
        for j in range(i, m):
            p2 = pm[j]
            if (not prime.IsPrime(CatNum(p1, p2))):
                continue
            if (not prime.IsPrime(CatNum(p2, p1))):
                continue
            cprime.add((p1, p2))

    logging.debug(len(cprime))
    ts3 = time.time()
    logging.debug("time for build prime pairs {}".format(ts3-ts2))

    for (p1, p2) in cprime:
        for p3 in pm:
            if (p3 <= p2): continue
            if (not Check(p3, [p1, p2], cprime)): continue
            for p4 in pm:
                if (p4 <= p3): continue
                if (not Check(p4, [p1, p2, p3], cprime)): continue
                for p5 in pm:
                    if (p5 <= p4): continue
                    if (not Check(p5, [p1, p2, p3, p4], cprime)): continue
                    logging.info((p1, p2, p3, p4, p5))
                    logging.info("result: {}".format(sum([p1, p2, p3, p4, p5])))
                    return 0
