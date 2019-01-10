# -*- coding: UTF-8 -*-
'''
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.
'''

import logging
logger = logging.getLogger('p105')

from util import check_optimum

def parse_set(fname):
    myset = []
    with open(fname) as f:
        for line in f:
            myset.append([int(x) for x in line.split(',')])
    return myset

def main(args):
    myset = parse_set("data/p105_sets.txt")
    answer = 0

    for i in range(2):
        logger.debug("check {}".format(myset[i]))
        logger.debug(check_optimum(myset[i], logger=logger, verbosity=1))

    for s in myset:
        if check_optimum(s):
            logger.debug(s)
            answer += sum(s)

    logger.info("answer: {}".format(answer))
