# -*- coding: UTF-8 -*-

#In the following equation x, y, and n are positive integers.
#1/x + 1/y = 1/n
#
#For n = 4 there are exactly three distinct solutions:
#1/5 + 1/20 = 1/4 
#1/6 + 1/12 = 1/4
#1/8 + 1/8 = 1/4
#It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.
#
#What is the least value of n for which the number of distinct solutions exceeds four million?
#
#NOTE: This problem is a much more difficult version of problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.

import logging
logger = logging.getLogger('p110')

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

def IsPrime(n):
    for p in primes:
        if (n%p == 0):
            return False
    return True

def AllPrimeFactorize(n):
    if (IsPrime(n)):
        return [n]
    for p in primes:
        if (n%p == 0):
            n = n//p
            if (n == 1):
                return [p]
            return [p] + AllPrimeFactorize(n)

def PrimeFactorizeDict(n):
    pf = AllPrimeFactorize(n)
    pfd = {}
    for p in pf:
        if p in pfd:
            pfd[p] += 1
        else:
            pfd[p] = 1
    return pfd

    
def NumDivisor(n):
    ''' return number of divisor'''
    pfd = PrimeFactorizeDict(n)
    nd = 1
    for (p, n) in pfd.items():
        nd = nd * (n+1)
    return nd

def NumSolutions(n):
    num_sol = 0
    for x in range(n+1, n*2+1):
        if (n*x%(x-n)==0):
            num_sol += 1
    return num_sol

def NumSol(n):
    return (NumDivisor(n*n)+1)//2

def main(args):
    k = 1000
    t = 2*3*5*7*11*13*17*19*23*29*31*37
    max_num_sol = 0
    for n in range(1, k*10):
        num_sol = NumSol(n*t)
        if (num_sol > max_num_sol):
            logger.debug('NumSol(%d) = %d' % (n*t, num_sol))
            logger.debug(AllPrimeFactorize(n*t))
            max_num_sol = num_sol
            if max_num_sol > 4000*1000:
                break

    logger.info("answer: {}".format(n*t))



