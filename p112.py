# -*- coding: UTF-8 -*-

#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
#Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first exceeds 50% is 538.
#
#Surprisingly bouncy number become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
#Find the least number for which the proportion of bouncy numbers is exactly 99%.

import logging
logger = logging.getLogger('p112')

from util import Digits

def IsBouncy(n):
    dn = Digits(n)
    inc = []
    dec = []
    for d in dn:
        inc.append(d)
        dec.append(d)
    inc.sort()
    dec.sort()
    dec.reverse()
    return dn != inc and dn != dec

def main(args):
    num_bouncy = 0
    for n in range(1,1000):
        if (IsBouncy(n)): num_bouncy += 1

    logger.debug(num_bouncy)

    num_bouncy = 0
    n = 100
    while (num_bouncy *100 < n*99):
        for i in range(100):
            n += 1
            if (IsBouncy(n)): num_bouncy += 1

    logger.debug(num_bouncy)
    logger.info("answer: {}".format(n))
