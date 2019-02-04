# Exploring Pascal's triangle
# Problem 148
#
# We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

#  	 	 	 	 	 	 1
#  	 	 	 	 	 1	 	 1
#  	 	 	 	 1	 	 2	 	 1
#  	 	 	 1	 	 3	 	 3	 	 1
#  	 	 1	 	 4	 	 6	 	 4	 	 1
#  	 1	 	 5	 	10	 	10	 	 5	 	 1
# 1	 	 6	 	15	 	20	 	15	 	 6	 	 1
# However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

# Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.

import logging
import pprint
from random import randint

from util import Digits

logger = logging.getLogger('p148')

def Pascal7(rows):
    pascal = [[1]]
    for r in range(rows-1):
        prow = pascal[-1]
        nrow = []
        for c in range(r+1):
            if c == 0:
                nrow.append(1)
            else:
                nrow.append((prow[c-1]+prow[c])%7)
        nrow.append(1)
        pascal.append(nrow)
    return pascal

def CountPascal7(rows):
    if rows <= 7:
        return rows*(rows+1)//2
    seven = 1
    cnt = 1
    r7 = rows // 7
    while seven <= r7:
        seven *= 7
        cnt *= 28
    q = rows // seven
    r = rows % seven
    return q*(q+1)*cnt//2 + (q+1)*CountPascal7(r)

def testCountPascal7(loop):
    while loop > 0:
        loop -= 1
        R = randint(100,10000)
        logger.debug("test {} rows, base7: {}".format(R, Digits(R, 7)))
        pt = Pascal7(R)
        cnt = 0
        for row in pt:
            for c in row:
                if c != 0:
                    cnt += 1
        cnt7 = CountPascal7(R)
        if cnt != cnt7:
            logger.info("rows:{} failed: expected {}, get {}".format(R, cnt, cnt7))

def main(args):
    
    if args.test:
        R = 100
        pt = Pascal7(R)
        answer = 0
        for row in pt:
            for c in row:
                if c != 0:
                    answer += 1
        testCountPascal7(10)

    else:
        K = 1000
        R = K*K*K
        logger.debug(Digits(R, 7))
        answer = CountPascal7(R)

    logger.info("answer: {}".format(answer))
