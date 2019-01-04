#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
#
#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
#Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

import logging
import time
from util import *
from prime import PrimeNumberPool

def IsPermute(a,b):
    da = Digits(a)
    db = Digits(b)
    da.sort()
    db.sort()
    return da == db

def main(args):
    if args.test:
        m = 100*1000
        maxprime = 1000
    else:
        m = 10*1000*1000
        maxprime = 100000

    t1 = time.time()
    prime = PrimeNumberPool(maxprime)
    t2 = time.time()
    logging.debug("time for build prime pool:{}".format(t2-t1))

    '''
    Analysis
    By observation, the numbers with high φ(n) are product of two prime numbers 
    '''
    max_ratio = (2, 1)
    num_prime = len(prime.numbers)
    for i in range(num_prime):
        p1 = prime.numbers[i]
        if p1*p1 > m:
            break
        for j in range(i, num_prime):
            p2 = prime.numbers[j]
            if p1*p2 > m:
                break
            n = p1*p2
            phi = n - p1 - p2 + 1
            if (IsPermute(n, phi)):
                if (max_ratio[0]*phi > max_ratio[1]*n):
                    logging.debug("{} factor to {}".format(n, prime.Factorize(n)))
                    max_ratio = (n, phi)
                    logging.debug(max_ratio)

    '''
    # brute force way
    for n in range(3,m,2):
        # pre-qualify
        pre_qualify = 1
        for p in prime.numbers:
            if (n % p == 0 and p*max_ratio[1] > (p-1)*max_ratio[0]):
                pre_qualify = 0
                break
            if (p * p > n):
                break
        if (pre_qualify):            
            pn = Phi(n,prime)
            if (IsPermute(n, pn)):
                if (max_ratio[0]*pn > max_ratio[1]*n):
                    logging.debug("{} factor to {}".format(n, prime.Factorize(n)))
                    max_ratio = (n, pn)
                    logging.debug(max_ratio)
    '''
    
    logging.info("answer: {}".format(max_ratio[0]))
