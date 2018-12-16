#

import os,logging
import time
import math
import re

def main(args):
    description = '''
    Special Pythagorean triplet
    Problem 9 
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    '''

    #
    # Analysis:
    # Pythagorean triplet: a = m^2-n^2, b = 2mn, c = m^2+n^2
    # a + b + c = 2m^2 + 2mn = 2m(m+n) = 1000 ==> m(m+n) = 500
    # m > n ==> 2m^2 > 500 > m^2 ==> 22 >= m >= 16
    # ==> m = 20
    #

    m = 20
    n = 500//m - m
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n

    solution = 'result: {}'.format(a*b*c)
    logging.info(solution)
