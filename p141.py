
# Investigating progressive numbers, n, which are also square
# Problem 141 
# https://projecteuler.net/problem=141
# 
# A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

# For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
# We will call such numbers, n, progressive.

# Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.
# The sum of all progressive perfect squares below one hundred thousand is 124657.

# Find the sum of all progressive perfect squares below one trillion (1012).

import math
from util import GCD
import logging
logger = logging.getLogger('p141')

# Analysis
#
# let r = ab^2, d = abc, q = ac^2, where b < c
# n^2 = r + dq = ab^2 + a^2bc^3
#

def cube_root(x):
    return math.pow(x, 1/3)

def main(args):
    K = 1000
    if args.test:
        N = 1000*K
    else:
        N = K*K*K*K

    C = int(cube_root(N))
    progressive_perfect_squares = []

    for c in range(2, C+1):
        c3 = c*c*c
        B = min(N//c3, c)
        for b in range(1, B):
            if GCD(b,c) > 1:
                continue
            A = int(math.sqrt(N//c3//b))
            for a in range(1, A):
                n2 = a*b*(b+a*c3)
                n = int(math.sqrt(n2))
                if n*n == n2:
                    progressive_perfect_squares.append(n2)
                    logger.debug("{} = {}^2 = {} + {}*{}".format(n2, n, a*b*b, a*b*c, a*c*c))

    answer = sum(list(set(progressive_perfect_squares)))
    logger.info("answer: {}".format(answer))
