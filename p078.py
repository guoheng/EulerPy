# -*- coding: UTF-8 -*-

#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O
#
#Find the least value of n for which p(n) is divisible by one million.
#
# reference http://en.wikipedia.org/wiki/Integer_partition

import logging

def main(args):
    if args.test:
        N = 10+1
        m = 7
    else:
        N = 100000
        m = 1000*1000

    p = list(range(4))
    p[0] = 1
    #Generalized pentagonal numbers 
    gpn = []
    sp = []
    for n in range(1,N):
        gpn.append(n*(3*n-1)//2)
        gpn.append(-n*(-3*n-1)//2)
        if (n%2 == 1):
            sp += [1,1]
        else:
            sp += [-1,-1]

    for n in range(4, N+1):  
        for g in range(N):
            if (gpn[g] > n): break
        pn = 0
        for i in range(g):
            pn += p[n-gpn[i]]*sp[i]
        p.append(pn)

    for i in range(N):
        if (p[i] % m == 0):
            logging.debug(p[i])
            logging.info("answer: {}".format(i))
            return 0
