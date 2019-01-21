# -*- coding: UTF-8 -*-

#Let r be the remainder when (a−1)n + (a+1)n is divided by a2.
#
#For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
#
#For 3 ≤ a ≤ 1000, find ∑ rmax.

# (a-1)^n + (a+1)^n ≡ 2 mod a^2 if n is even
# (a-1)^n + (a+1)^n ≡ 2*n*a mod a^2 if n is odd 

import logging
logger = logging.getLogger('p120')

def MaxRemainder(a):
    remainder = 2
    a2 = a*a
    for n in range(1, a2, 2):
        r = 2*n*a % a2
        if r > remainder:
            remainder = r
    return remainder

def main(args):

    sum_rmax = 0
    for a in range(3, 1001):
        if (a%2 == 1):
            rmax = a*(a-1)
        else:
            rmax = a*(a-2)
        sum_rmax += rmax

    logger.info("answer: {}".format(sum_rmax))
