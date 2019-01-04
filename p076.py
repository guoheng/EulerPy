# -*- coding: UTF-8 -*-

#It is possible to write five as a sum in exactly six different ways:
#
#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1
#
#How many different ways can one hundred be written as a sum of at least two positive integers?
import logging

num_sum = {}

def NumSum(n, m=1):
    if (n < m*2): return 0
    if (n == m*2): return 1
    if ((n,m) in num_sum): return num_sum[(n,m)]
    s = 0
    for i in range(m,n//2+1):
        s += NumSum(n-i, i)+1
    num_sum[(n,m)] = s
    return s

def main(args):
    if args.test:
        L = 5
    else:
        L = 100

    logging.info('answer: {}'.format(NumSum(L)))
