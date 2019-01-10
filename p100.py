# -*- coding: UTF-8 -*-

#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
#
#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
#
#By finding the first arrangement to contain over 10^(12) = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

from math import sqrt
import logging
logger = logging.getLogger('p100')

"""
Find solution for 2b(b-1) = (r+b)(r+b-1) = m(m-1)
find a close pair (b, m) such that 
    2b^2 =~ m^2
    m =~ b sqrt(2)
    sqrt2 =~ m/b

    Hint: Continued fraction representation of sqrt(2)
    start with 
    m = [3]
    b = [2]
    expand with iteration
    m[n] = 2b[n-1]+m[n-1]
    b[n] = b[n-1]+m[n-1]
    then
    sqrt(2) is approximated by m[n]/b[n]

"""

def main(args):
    sqrt2 = sqrt(2)

    a =[5]
    b = [12,70]
    for i in range(9):
        bn = 6*b[-1]-b[-2]
        b.append(bn)

    for i in b:
        an = a[-1]+i
        an1 = an+i
        a += [an, an1]
            
    logger.debug(a)
    logger.debug(b)

    blue = []
    tot = []
    for i in range(len(a)-1):
        n = a[i]*a[i+1]
        m = int(n*sqrt2)
        logger.debug("%d*%d - 2*%d*%d = %d" % (m, m-1, n, n-1, m*(m-1)-2*n*(n-1)))
        blue.append(n)
        tot.append(m)

    logger.debug(blue)

    for i in range(len(blue)):
        if (tot[i] > 10**12):
            logger.debug("answer:{}".format(blue[i]))
            break
