# -*- coding: UTF-8 -*-

#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
#
#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
#
#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

import logging
from math import sqrt

def SqrtDigits(n, m):
    q = int(sqrt(n))
    qn = q
    if (q*q == n): return 0
    r = (n-q*qn)*100
    for i in range(m):
        qn = r//(q*20)
        if (qn*(q*20+qn) > r): qn -= 1
        r = (r - qn*(q*20+qn))*100
        q = q*10+qn
    return q

def SumDig(n):
    s = 0
    while (n):
        s += n%10
        n = n//10
    return s

def main(args):

    s = 0
    for n in range(2,100):
        s += SumDig(SqrtDigits(n, 99))

    logging.info("answer: {}".format(s))


