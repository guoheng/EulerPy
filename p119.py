# -*- coding: UTF-8 -*-

#The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.
#
#We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
#
#You are given that a2 = 512 and a10 = 614656.
#
#Find a30.

from util import Digits
import logging
logger = logging.getLogger('p119')

def IsPowerSum(n):
    s = sum(Digits(n))
    if s == 1:
        return False
    while (n > 1):
        if (n % s == 0):
            n = n//s
        else:
            return False
    return True

def main(args):
    k = 1000
    m = k*k
    cnt = 0
    for n in range(10, m):
        if (IsPowerSum(n)):
            cnt += 1
            logger.debug((cnt, n))
            if cnt > 30:
                break

    aps = []
    ap30 = 1<<100
    for a in range(2,k):
        for p in range(2,100):
            ap = a**p
            if ap > ap30: 
                break
            if sum(Digits(ap)) == a:
                logger.debug('%d^%d = %d' % (a, p, ap))
                aps.append(ap)
                if (len(aps)>=30):
                    aps.sort()
                    ap30 = aps[29]
                    logger.debug('a30 = {}'.format(ap30))

    aps.sort()
    logger.debug(aps)
    logger.info('a30 = {}'.format(aps[29]))
