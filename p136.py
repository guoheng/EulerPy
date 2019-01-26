
# Singleton differences
# Problem 135 

# The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer, the equation, x2 − y2 − z2 = n, has exactly one solution when n = 20:

# 132 − 102 − 72 = 20

# In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

# How many values of n less than fifty million have exactly one solution?

# Analysis
# let x = y+d, z = y-d
# x^2 - y^2 - z^2 = y(4d-y) = n
# node thant 
#  z > 0 ---> y > d
#  n > 0 ---> 4d-y > 0
# if (y, d) is a solution, then (4d-y, d) is also a solution 
# unless 4d-y < d, which is y > 3d or y = 2d


import logging
logger = logging.getLogger('p136')

def main(args):
    
    if args.test:
        K = 100
        N = 100*K*K
    else:
        K = 1000
        N = 50*K*K

    solutions = dict()

    for y in range(1, N):
        for d in range(y//4+1, y):
            n = y*(4*d-y)
            if n >= N:
                break
            if n in solutions:
                solutions[n] += 1
            else:
                solutions[n] = 1

    sol1 = []
    for k,v in solutions.items():
        if v == 1:
            sol1.append(k)
            if args.verbosity > 2:
                logger.debug("n={}".format(k))
                logger.debug(v)
    
    answer = len(sol1)
    logger.info("answer: {}".format(answer))
