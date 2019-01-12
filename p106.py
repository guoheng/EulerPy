# -*- coding: UTF-8 -*-
'''
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

'''

import logging
logger = logging.getLogger('p106')

from util import select

def check_pair_to_cmp(s1, s2):
    s1.sort()
    s2.sort()
    cmp_dir = s1[0] > s2[0]
    for i in range(1, len(s1)):
        next_cmp_dir = s1[i] > s2[i]
        if next_cmp_dir != cmp_dir:
            return True
    return False

def check_overlap(s1, s2):
    for i in s2:
        if i in s1:
            return True
    return False

def find_subset_pair(n):
    s = list(range(n))
    cmp_cnt = 0
    for i in range(len(s)//2):
        subset = select(i+1, s)
        l = len(subset)
        for j in range(l-1):
            s1 = subset[j]
            s1.sort()
            for k in range(j+1, l):
                s2 = subset[k]
                if check_overlap(s1, s2):
                    continue
                s2.sort()
                if check_pair_to_cmp(s1, s2):
                    cmp_cnt += 1
    return cmp_cnt

def main(args):
    answer = 0

    logger.debug(find_subset_pair(4))
    logger.debug(find_subset_pair(7))

    answer = find_subset_pair(12)
    logger.info("answer: {}".format(answer))
