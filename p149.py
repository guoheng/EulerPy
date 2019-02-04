# Searching for a maximum-sum subsequence
# Problem 149
# https://projecteuler.net/problem=149

import numpy as np
from util import max_subarray
import logging
logger = logging.getLogger('p149')

def LaggedFibonacciGenerator():
    # For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
    # For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000
    s = []
    for k in range(1, 56):
        sk = 100003 - 200003*k + 300007*k*k*k
        s.append( sk % 1000000 - 500000)
    for k in range(56, 4000001):
        sk = (s[k-24-1] + s[k-55-1] + 1000000)
        s.append( sk % 1000000 - 500000)
    return s

def main(args):
    N = 2000
    s = LaggedFibonacciGenerator()
    mat = np.array(s).reshape((N, N))

    # max sum in horizontal
    sub_sum_h = []
    for r in range(N):
        row = mat[r].tolist()
        sub_sum_h.append(max_subarray(row))
    max_sum_h = max(sub_sum_h)
    logger.debug("horizontal max sum: {}".format(max_sum_h))

    # max sum in vertical
    sub_sum_v = []
    for c in range(N):
        col = mat[:,c].tolist()
        sub_sum_v.append(max_subarray(col))
    max_sum_v = max(sub_sum_v)
    logger.debug("vertical max sum: {}".format(max_sum_v))

    # max sum in up-left
    sub_sum_ul = []
    for r in range(N):
        a = []
        for c in range(N-r):
            a.append(mat[r+c,c])
        sub_sum_ul.append(max_subarray(a))
    for c in range(1, N):
        a = []
        for r in range(N-c):
            a.append(mat[r, r+c])
        sub_sum_ul.append(max_subarray(a))
    max_sum_ul = max(sub_sum_ul)
    logger.debug("up-left max sum: {}".format(max_sum_ul))

    # max sum in up-right
    sub_sum_ur = []
    for r in range(N):
        a = []
        for c in range(r+1):
            a.append(mat[r-c,c])
        sub_sum_ur.append(max_subarray(a))
    for c in range(1, N):
        a = []
        for r in range(N-1, c-1,-1):
            a.append(mat[r,N-c-r])
        sub_sum_ur.append(max_subarray(a))
    max_sum_ur = max(sub_sum_ur)
    logger.debug("up-right max sum: {}".format(max_sum_ur))


    answer = max([max_sum_h, max_sum_v, max_sum_ul, max_sum_ur])
    logger.info("answer: {}".format(answer))
