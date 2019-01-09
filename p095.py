# -*- coding: UTF-8 -*-

#The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
#
#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
#
#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
#
#12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
#
#Since this chain returns to its starting point, it is called an amicable chain.
#
#Find the smallest member of the longest amicable chain with no element exceeding one million.

from prime import PrimeNumberPool
import logging
import time

logger = logging.getLogger('p095')
prime = PrimeNumberPool()

amicable_cache = dict()
divisors_cache = {}

def SumDivisor(n):
    if n in divisors_cache:
        mydivisors = divisors_cache[n]
    else:
        mydivisors = prime.getDivisor(n)
        divisors_cache[n] = mydivisors
    return sum(mydivisors)-n

def AmicableChain(n, MAX_NUM=1000000):
    if (n > MAX_NUM):
        return []
    ac = [n]
    set_ac = set(ac)
    sdn = SumDivisor(n)
    while (not sdn in set_ac):
        if (sdn > MAX_NUM):
            return []
        ac.append(sdn)
        set_ac.add(sdn)
        sdn = SumDivisor(sdn)
        if sdn in amicable_cache:
            return amicable_cache[sdn]
        if sdn == 0:
            for i in ac:
                amicable_cache[i] = []
            return []
    idx = ac.index(sdn)
    for i in ac:
        amicable_cache[i] = ac[idx:]
    return ac[idx:]

def main(args):
    prime.FillTo(100000)

    if args.test:
        for n in [28, 220, 12496, 94520]:
            logger.debug("{} Amicable chains: {}".format(n, AmicableChain(n)))
        return 0
    else:
        k = 1000
        m = k*200

    long_ac = []
    ac_time = 0.03
    cache_hit = 0
    for n in range(17, m):
        if n in prime.numbers:
            cache_hit += 1
            continue
        if n in amicable_cache:
            ac = amicable_cache[n]
            cache_hit += 1
        else:
            ts1 = time.time()
            ac = AmicableChain(n)
            ts2 = time.time()
            if ts2-ts1 > ac_time:
                logger.debug("AmicableChain({}) takes {}s".format(n, ts2-ts1))
                ac_time = ts2-ts1
        if (len(ac) > len(long_ac)):
            long_ac = ac
            logger.debug(long_ac)

    long_ac.sort()
    logger.info("answer: {}".format(long_ac[0]))
    logger.debug("amicable_cache hit:{}".format(cache_hit))
