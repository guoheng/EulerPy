
# Prime pair connection
# Problem 134 
# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

# Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

import pickle
import time
from prime import PrimeNumberPool
from util import ExtendedEuclidean
import logging
logger = logging.getLogger('p134')

primes = PrimeNumberPool()

def S(p1, p2):
    t = 10
    while t < p1:
        t *= 10
    # find out n*t+p1 = 0 (mod p2)
    # n*t = p2-p1 mod p2
    # n*t = k*p2 = (p2-p1)
    # since GCD(t, p2) = 1,
    # we can find x*t+y*p2 = 1
    # then n = x*(p2-p1), k = y*(p2=p1)
    x, y = ExtendedEuclidean(t, p2)
    n = (x*(p2-p1)%p2)*t+p1
    return n

def main(args):

    if args.test:
        K = 10
        M = K*K
    else:
        K = 1000
        M = K*K

    ts1 = time.time()
    with open("data/prime_numbers.pkl", 'rb') as f:
        primes.numbers = pickle.load(f)
    ts2 = time.time()
    logger.debug("setup time:{}".format(ts2-ts1))

    ss = []
    for i in range(2, len(primes.numbers)-1):
        p1 = primes.numbers[i]
        if p1 > M:
            break
        p2 = primes.numbers[i+1]
        s = S(p1, p2)
        ss.append(s)
        if args.verbosity > 2:
            logger.debug("S({}, {}) = {}".format(p1, p2, s))

    logger.debug(ss)
    answer = sum(ss)
    logger.info("answer: {}".format(answer))
