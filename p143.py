
# Investigating the Torricelli point of a triangle
# Problem 143 
# https://projecteuler.net/problem=143
# 
# 

from math import sqrt
from util import GCD
import time
import pprint

import logging
logger = logging.getLogger('p143')

# Analysis
# the angle between p,q,r is 120, so
# a^2 = q^2+r^2+qr
# b^2 = p^2+q^2+pq
# c^2 = r^2+p^2+rp

def IsSqrt(n):
    s = int(sqrt(n))
    return s*s == n

def getEdge(p, q):
    e2 = p*p+q*q+p*q
    e = int(sqrt(e2))
    if e*e == e2:
        return e
    else:
        return -1

def main(args):

    if args.test:
        L = 32000
        brute_force = True
    else:
        L = 120000
        brute_force = False

    if brute_force:
        ts1 = time.time()
        bsol = dict()
        for p in range(1, L//3+1):
            for q in range(p+1, (L-p)//2+1):
                b = getEdge(p, q)
                if b < 0:
                    continue
                for r in range(q+1, L-p-q+1):
                    a = getEdge(q, r)
                    if a < 0:
                        continue
                    c = getEdge(r, p)
                    if c > 0 and p+q+r <= L:
                        k = "{},{},{}".format(p,q,r)
                        bsol[k] = (a, b, c, p, q, r)
        logger.debug(bsol)
        sum_pqr = 0
        for k, v in bsol.items():
            a,b,c,p,q,r = v
            s = p+q+r
            if s <= L:
                sum_pqr += s
        logger.debug("answer: {}".format(sum_pqr))
        logger.debug("brute force time: {}".format(time.time()-ts1))
        ts1 = time.time()

    pqb = dict()
    cache = dict()
    ts1 = time.time()
    for p in range(3, L//3):
        if p in pqb:
            cache_q = [x[1] for x in pqb[p]]
        else:
            cache_q = []
        for q in range(p+1, L-p*2):
            if len(cache_q) > 0 and q in cache_q:
                continue      
            b = getEdge(p, q)
            if b > 0:
                for s in range(1, L//(p+q)+1):
                    ps, qs, bs = p*s, q*s, b*s
                    k = "{},{}".format(ps,qs)
                    cache[k] = [ps, qs, bs]
                    if ps in pqb:
                        pqb[ps].append((ps, qs, bs))
                    else:
                        pqb[ps] = [(ps, qs, bs)]
                    
    ts2 = time.time()
    logger.debug("compute possible p, q: {}".format(ts2-ts1))
    logger.debug("possible p, q: {}".format(len(pqb)))

    solution = dict()
    for p, v in pqb.items():
        qs = [x[1] for x in v]
        n = len(qs)
        for i in range(n-1):
            q = qs[i]
            b = v[i][2]
            for j in range(i+1, n):
                r = qs[j]
                c = v[j][2]
                a = getEdge(q, r)
                if a >0:
                    key = "{},{},{}".format(p,min(q,r), max(q,r))
                    solution[key] = (a,b,c,p,min(q,r), max(q,r))

    logger.debug(pprint.pformat(solution))

    if brute_force:
        for k, v in bsol.items():
            if k not in solution:
                logger.debug("missed {}".format(v))

    pqr = []
    for k, v in solution.items():
        a,b,c,p,q,r = v
        s = p+q+r
        if s <= L:
            pqr.append(s)
    
    logger.debug("sum(pqr)={}".format(sum(pqr)))

    answer = sum(list(set(pqr)))
    logger.info("answer: {}".format(answer))
