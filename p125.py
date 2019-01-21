# -*- coding: UTF-8 -*-

#The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
#
#There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
#
#Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.

from util import IsPalindromic

import logging
logger = logging.getLogger('p125')

def main(args):

    k = 1000
    m = k*10
    max_p = m*m

    square = []
    for n in range(m):
        square.append(n*n)
        
    palindromic_square = []
    set_palindromic_square = set()
    for i in range(1, m-1):
        sq_sum = square[i]
        for j in range(i+1, m):
            sq_sum += square[j]
            if (sq_sum > max_p):
                break
            if (IsPalindromic(sq_sum)):
                logger.debug('%d = sum(%d^2, %d^2)' % (sq_sum, i, j))
                if (not sq_sum in set_palindromic_square):
                    palindromic_square.append(sq_sum)
                    set_palindromic_square.add(sq_sum)

    logger.debug(palindromic_square)
    logger.info("answer: {}".format(sum(palindromic_square)))
