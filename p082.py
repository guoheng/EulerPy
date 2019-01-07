# -*- coding: UTF-8 -*-

#NOTE: This problem is a more challenging version of Problem 81.
#
#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red; the sum is equal to 994.
#
#    
#131    673    234    103    18
#201    96    342    965    150
#630    803    746    422    111
#537    699    497    121    956
#805    732    524    37    331
#    
#
#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

import logging
from util import parse_matrix

def main(args):
    mtx = parse_matrix("data/p082_matrix.txt")
    n = len(mtx)


    # rotate the matrix so the path go from top down
    for i in range(n-1):
        for j in range(i+1, n):
            (mtx[i][j], mtx[j][i]) = (mtx[j][i], mtx[i][j])

    min_p = list(range(n))
    for i in range(1, n):
        for j in range(n):
            min_p[j] = mtx[i][j]+mtx[i-1][j]
            for k in range(n):
                if (k == j): continue
                if (k < j):
                    sum_kj = mtx[i-1][k] + sum(mtx[i][k:j+1])
                    if (min_p[j] > sum_kj): min_p[j] = sum_kj
                else:
                    sum_jk = mtx[i-1][k] + sum(mtx[i][j:k+1])
                    if (min_p[j] > sum_jk): min_p[j] = sum_jk
        for j in range(n):
            mtx[i][j] = min_p[j]
            
    logging.debug(min_p)
    min_sp = min_p[0]
    for i in range(n):
        if (min_sp > min_p[i]): min_sp = min_p[i]
    logging.info("answer: {}".format(min_sp))


