
# Perfect Square Collection
# Problem 142 
# https://projecteuler.net/problem=142
# 
# Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.

from math import sqrt
import logging
logger = logging.getLogger('p142')

# Analysis
# let y-z = a^2, y+z = b^2
# then y -=(a^2+b^2)/2; z = (b^2-a^2)/2
# let x-z = c^2, x+z = d^2
# then x = (c^2+d^2)/2; z = (d^2-c^2)/2


def IsSqrt(n):
    s = int(sqrt(n))
    return s*s == n

def main(args):

    K = 1000
    N = K*2

    squares = [i*i for i in range(N+1)]

    sq_diff = dict()
    for i in range(1, N-1):
        for j in range(i+1, N):
            if j % 2 != i % 2:
                continue
            mydiff = squares[j] - squares[i]
            if mydiff in sq_diff:
                sq_diff[mydiff].append([i, j])
            else:
                sq_diff[mydiff] = [[i, j]]
    
    solution = []
    for k, v in sq_diff.items():
        z = k//2
        n = len(v)
        for i in range(n-1):
            a, b = v[i]
            y = (a*a+b*b)//2
            for j in range(i+1, n):
                c, d = v[j]
                x = (c*c+d*d)//2
                if x < y:
                    x, y = y, x
                if IsSqrt(x+y) and IsSqrt(x-y):
                    solution.append([x,y,z, x+y+z])
                    logger.debug((k, v))

    logger.debug(solution)


    answer = min([x[3] for x in solution])
    logger.info("answer: {}".format(answer))
