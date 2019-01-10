#!/usr/bin/env python
#
# -*- coding: UTF-8 -*-
#
# caculate the prime numbers
from __future__ import print_function
from __future__ import division
from __future__ import with_statement

import random
from prime import PrimeNumberPool
import logging

# return a list with unique items
def Unique(my_list):
    return list(set(my_list))

# premutation of a string
def all_perms(my_str):
    if len(my_str) <=1:
        yield my_str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + my_str[0:1] + perm[i:]

#
# Euler's Totient function, φ(n) [sometimes called the phi function], is used
# to determine the number of positive numbers less than or equal to n which 
# are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all 
# less than nine and relatively prime to nine, φ(9)=6.
#

def Phi(n, prime):
    factors = prime.getPrimeFactor(n)
    if len(factors) == 1:
        return n - n//factors[0]
    elif len(factors) == 2:
        p1, p2 = factors
        return n - n//p1 - n//p2 + n//p1//p2
    cnt = [1]*n
    for p in factors:
        for i in range(n//p):
            cnt[i*p-1] = 0
    return sum(cnt)

#
# return all digits of a number
#
def Digits(n):
    d = []
    while (n):
        d.append(n%10)
        n = n//10
    return d

# roll a dice d n times
def RollDice(n, d):
    dices = []
    for i in range(n):
        dices.append(random.randint(1,d))
    return dices

def Product(list):
    p = list[0]
    for x in list[1:]:
        p *= x
    return p

def IsPalindromic(n):
    sn = str(n)
    return sn == sn[::-1]

def parse_matrix(fname):
    matrix = []
    with open(fname) as f:
        for line in f.readlines():
            matrix.append([int(x) for x in line.split(',')])
    return matrix

# select n items from l
def select(n, l):
    if (n > len(l)): return []
    if (n == len(l)):
        return [l]
    r = []
    if (n == 1):
        for i in l:
            r.append([i])
        return r
    r1 = select(n-1, l[1:])
    for s in r1:
        s.append(l[0])
    r = r1
    return r + select(n, l[1:])

# for problem 103,105
def check_optimum(s, logger=logging.getLogger(), verbosity=0):
    if len(s) < 3:
        return True
    mysum = {}
    for i in range(len(s)-1):
        subset = select(i+1, s)
        mysum[i] = [sum(x) for x in subset]
        if len(mysum[i]) > len(set(mysum[i])):
            return False
    for i in range(len(s)-2):
        sum1 = max(mysum[i])
        sum2 = min(mysum[i+1])
        if sum1 >= sum2:
            return False

    return True
