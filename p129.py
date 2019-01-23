
# Repunit divisibility
# Problem 129 
# A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

# Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, 
# and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

# The least value of n for which A(n) first exceeds ten is 17.

# Find the least value of n for which A(n) first exceeds one-million.

import logging
logger = logging.getLogger('p129')

def A(n):
    m = 1
    k = 1
    mk = 1
    while m != 0:
        k += 1
        mk = mk*10%n
        m = (m+mk) % n
    return k

def main(args):
    if args.test:
        N = 10
        for n in [7, 41]:
            logger.debug("A({}) = {}".format(n, A(n)))
    else:
        N = 1000*1000
    
    t = N//10-2
    done = False
    maxk = 0
    while not done:
        t += 1
        for d in [1, 3, 7, 9]:
            n = t*10+d
            an = A(n)
            if an > maxk:
                logger.debug("A({}) = {}".format(n, an))
                maxk = an
            if an > N:
                done = True
                break
    
    answer = n
    logger.info("answer: {}".format(answer))
