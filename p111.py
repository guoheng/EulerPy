# -*- coding: UTF-8 -*-
"""
Primes with runs
Problem 111 
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d	M(4, d)	N(4, d)	S(4, d)
0	2	13	67061
1	3	9	22275
2	3	1	2221
3	3	12	46214
4	3	2	8888
5	3	1	5557
6	3	1	6661
7	3	9	57863
8	3	1	8887
9	3	7	48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""

import time
from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p111')

prime = PrimeNumberPool(120000)

def M1(n, d):
    N = []
    dd = d*(10**n-1)//9
    n0 = 10**(n-1)
    for a in range(10):
        for i in range(n):
            k = dd + (a-d)*(10**i)
            if k < n0:
                continue
            if prime.IsPrime(k):
                N.append(k)
    return N

def M2(n, d):
    N = []
    dd = d*(10**n-1)//9
    n0 = 10**(n-1)
    for a in range(10):
        for b in range(10):
            for i in range(n-1):
                for j in range(i+1, n):
                    k = dd + (a-d)*(10**i) + (b-d)*(10**j)
                    if k < n0:
                        continue
                    if prime.IsPrime(k):
                        N.append(k)
                        if a == d or b == d:
                            return []
    return N

def main(args):
    N4 = []
    for d in range(10):
        m1 = M1(4,d)
        if len(m1) > 0:
            N4.append(m1)
            logger.debug("M(4, {}) = 3; N(4, {}) = {})".format(d, d, len(m1)))
        else:
            m2 = M2(4, d)
            N4.append(m2)
            logger.debug("M(4, {}) = 2; N(4, {}) = {})".format(d, d, len(m2)))
    
    logger.debug(N4)
    logger.debug(sum(sum(x) for x in N4))

    N = []
    for d in range(10):
        m1 = M1(10,d)
        if len(m1) > 0:
            N.append(m1)
            logger.debug("M(10, {}) = 9; N(10, {}) = {})".format(d, d, len(m1)))
        else:
            m2 = M2(10, d)
            N.append(m2)
            logger.debug("M(10, {}) = 8; N(10, {}) = {})".format(d, d, len(m2)))
    
    logger.debug(N)

    answer = sum(sum(x) for x in N)
    logger.info("answer: {}".format(answer))

