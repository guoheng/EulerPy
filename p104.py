# -*- coding: UTF-8 -*-

#The Fibonacci sequence is defined by the recurrence relation:
#
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
#It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
#
#Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

import logging
logger = logging.getLogger('p104')

from util import Digits

def pandigital(ds):
    ds.sort()
    return ds == list(range(1,10))

t9 = 1000*1000*1000
def last9digits(n):
    n9 = n%t9
    return Digits(n9)

def isPandigital(n9):
    s9 = set([])
    for i in range(9):
        last_d = n9%10
        if (last_d == 0):
            return False
        if (last_d in s9):
            return False
        s9.add(last_d)
        n9 = n9//10
    return True

def main(args):
    last9_1 = last9_2 = 1
    k = 400000
    fn1 = fn2 = 1
    for i in range(k):
        fn = fn1 + fn2
        last9 = (last9_1 + last9_2)%t9
        if (isPandigital(last9)):
            logger.debug('''f(%d) last nine pandigital '''%(i+3))
            tmp = fn
            for j in range(i//20):
                tmp = tmp//10000
            dn = Digits(tmp)
            if (pandigital(dn[-9:])):
                logger.debug('''f(%d) first nine pandigital '''%(i+3))
                break
        fn2 = fn1
        fn1 = fn
        last9_2 = last9_1
        last9_1 = last9
        
    logger.info("answer: {}".format(i+3))
