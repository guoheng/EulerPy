
# Repunit nonfactors
# Problem 133 
# A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

# Let us consider repunits of the form R(10n).

# Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. Yet there is no value of n for which R(10n) will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10n).

# Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).

import time
from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p133')

primes = PrimeNumberPool()

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
        N = 100
    else:
        N = 100000

    ts1 = time.time()
    primes.FillTo(N)
    ts2 = time.time()
    logger.debug("setup time:{}".format(ts2-ts1))
    rnf = [2,3,5]
    for p in primes.numbers[3:]:
        if p > N:
            break
        ap = A(p)
        apf = primes.getPrimeFactor(ap)
        if len(apf) == 1 and apf[0] in [2,5]:
            continue
        if apf == [2, 5]:
            continue
        rnf.append(p)

    logger.debug(rnf)
    answer = sum(rnf)
    logger.info("answer: {}".format(answer))
