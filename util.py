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
