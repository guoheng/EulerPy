# -*- coding: UTF-8 -*-

#In the following equation x, y, and n are positive integers.
#1/x + 1/y = 1/n
#
#For n = 4 there are exactly three distinct solutions:
#1/5 + 1/20 = 1/4 
#1/6 + 1/12 = 1/4
#1/8 + 1/8 = 1/4
#What is the least value of n for which the number of distinct solutions exceeds one-thousand?

from prime import PrimeNumberPool
import logging
logger = logging.getLogger('p108')

def NumSolutions(n):
    num_sol = 0
    for x in range(n+1, n*2+1):
        if (n*x%(x-n)==0):
            num_sol += 1
    return num_sol

def main(args):
    k = 1000
    t = 2*2*3*3*5
    answer = 0
    for n in range(1, k*10):
        num_sol = NumSolutions(n*t)
        if (num_sol > 700):
            logger.debug('NumSolutions(%d) = %d' % (n*t, num_sol))
        if num_sol > 1000:
            answer = n*t
            break
    
    logger.info("answer: {}".format(answer))
