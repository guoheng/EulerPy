# -*- coding: UTF-8 -*-

#By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic 
# operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.
#
#For example,
#
#8 = (4 * (1 + 3)) / 2
#14 = 4 * (3 + 1 / 2)
#19 = 4 * (2 + 3) − 1
#36 = 3 * 4 * (2 + 1)
#
# Note that concatenations of the digits, like 12 + 34, are not allowed.
#
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, 
# and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
#
# Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, 
# can be obtained, giving your answer as a string: abcd.

import permute
import re
import logging

logger = logging.getLogger('p093')

ops = "+-*/"
r1 = re.compile("\*1\.0")

def IsInteger(x):
    return(x-int(x)==0)


def Form3Ops():
    three_ops = []
    for i in ops:
        if i == '/': i = '*1.0/'
        for j in ops:
            if j == '/': j = '*1.0/'
            for k in ops:
                if k == '/': k = '*1.0/'
                three_ops.append([i,j,k])
    return three_ops
     
def FormExpression(my_str):
    three_ops = Form3Ops()
    expressions = []
    for n in permute.all_perms(my_str):
        a = str(n[0])
        b = str(n[1])
        c = str(n[2])
        d = str(n[3])
        for op in three_ops:
            my_express = a+op[0]+b+op[1]+c+op[2]+d
            expressions.append(my_express)
            my_express = '('+a+op[0]+b+')'+op[1]+c+op[2]+d
            expressions.append(my_express)
            my_express = '('+a+op[0]+b+op[1]+c+')'+op[2]+d
            expressions.append(my_express)
            my_express = a+op[0]+'('+b+op[1]+c+')'+op[2]+d
            expressions.append(my_express)
            my_express = a+op[0]+'('+b+op[1]+c+op[2]+d+')'
            expressions.append(my_express)
            my_express = a+op[0]+b+op[1]+'('+c+op[2]+d+')'
            expressions.append(my_express)
            my_express = '('+a+op[0]+b+')'+op[1]+'('+c+op[2]+d+')'
            expressions.append(my_express)
            my_express = '(('+a+op[0]+b+')'+op[1]+c+')'+op[2]+d
            expressions.append(my_express)
            my_express = '('+a+op[0]+'('+b+op[1]+c+'))'+op[2]+d
            expressions.append(my_express)
            my_express = a+op[0]+'(('+b+op[1]+c+')'+op[2]+d+')'
            expressions.append(my_express)
            my_express = a+op[0]+'('+b+op[1]+'('+c+op[2]+d+'))'
            expressions.append(my_express)
    return expressions


def FindIntExpress(str):
    s_rslt = set()
    for e in FormExpression(str):
        try:
            x = eval(e)
        except:
            pass
        if x < 0:
            continue
        if IsInteger(x):
            r = int(x)
            if not (r in s_rslt):
                s_rslt.add(r)
    return s_rslt

def LongestConsecutive(s_rslt):
    assert(type(s_rslt)==set)
    n = 1
    while (n in s_rslt):
        n += 1
    return n-1
    
def main(args):
    longest_consecutive = 0

    for a in range(1,7):
        for b in range(a+1, 8):
            for c in range(b+1, 9):
                for d in range(c+1, 10):
                    my_expr = FindIntExpress([a,b,c,d])
                    my_lc = LongestConsecutive(my_expr)
                    if my_lc > longest_consecutive:
                        longest_consecutive = my_lc
                        logger.debug("{}, {}, {}".format([a,b,c,d], longest_consecutive, my_expr))
                        answer = "answer: {}{}{}{}".format(a,b,c,d)

    logger.info(answer)
