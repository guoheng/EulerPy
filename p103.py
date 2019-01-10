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
logger = logging.getLogger('p103')

from util import check_optimum

def main(args):
    s3 = [2,3,4]
    logger.debug("{} optimum set? {}".format(s3, check_optimum(s3)))
    s4 = [3, 5, 6, 7]
    logger.debug("{} optimum set? {}".format(s4, check_optimum(s4)))
    s5 = [6, 9, 11, 12, 13]
    logger.debug("{} optimum set? {}".format(s5, check_optimum(s5)))
    s6 = [11, 17, 20, 22, 23, 24]
    logger.debug("{} optimum set? {}".format(s6, check_optimum(s6)))
    s6 = [11, 17, 19, 20, 22, 25]
    logger.debug("{} optimum set? {}".format(s6, check_optimum(s6, logger=logger, verbosity=1)))
    s6 = [11, 18, 19, 20, 22, 25]
    logger.debug("{} optimum set? {}".format(s6, check_optimum(s6)))

    s6m = 18
    s7 = [s6m]
    s7 += [x+s6m for x in s6]
    logger.debug("{} optimum set? {}".format(s7, check_optimum(s7, logger=logger, verbosity=1)))

    s7 = [18, 28, 35, 36, 37, 39, 42]
    logger.debug("{} optimum set? {}".format(s7, check_optimum(s7, logger=logger, verbosity=1)))

    s7 = [19, 29, 36, 37, 38, 40, 43]
    logger.debug("{} optimum set? {}".format(s7, check_optimum(s7, logger=logger, verbosity=1)))

    s6m = 19
    s7 = [s6m]
    s7 += [x+s6m for x in s6]
    logger.debug("{} optimum set? {}".format(s7, check_optimum(s7)))

    s6m = 20
    s7 = [s6m]
    s7 += [x+s6m for x in s6]
    logger.debug("{} optimum set? {}".format(s7, check_optimum(s7)))

    t7 = [
        [19, 26, 31, 33, 35, 36, 39],
        [19, 27, 32, 35, 37, 38, 39],
        [19, 27, 34, 35, 36, 38, 41],
        [19, 28, 33, 35, 37, 38, 41],
        [19, 28, 33, 36, 38, 39, 40],
        [19, 28, 35, 36, 37, 39, 42],
        [19, 29, 34, 36, 38, 39, 42],
        [19, 29, 34, 37, 39, 40, 41],
        [19, 29, 36, 37, 38, 40, 43]
    ]

    for t in t7:
        logger.debug("{} optimum set? {}".format(t, check_optimum(t, logger=logger, verbosity=1)))

    t = [19, 30, 37, 38, 39, 41, 44]
    logger.debug("{} optimum set? {}".format(t, check_optimum(t, logger=logger, verbosity=1)))

    # find the minimised s7
    candidate = []
    for a0 in range(17, 21):
        for a1 in range(a0+1, a0+12):
            for a2 in range(a1+1, a1+9):
                for a3 in range(a2+1, a2+4):
                    for a4 in range(a3+1, a3+4):
                        for a5 in range(a4+1, a4+4):
                            for a6 in range(a5+1, a5+4):
                                s7 = [a0, a1, a2, a3, a4, a5, a6]
                                if check_optimum(s7):
                                    logger.debug(s7)
                                    candidate.append(s7)
                                    logger.debug(''.join([str(x) for x in s7]))

    mysum = sum(candidate[0])
    answer = candidate[0]
    for c in candidate:
        sumc = sum(c)
        if sumc < mysum:
            mysum = sumc
            answer = c

    logger.info("answer: {}".format(''.join([str(x) for x in answer])))
