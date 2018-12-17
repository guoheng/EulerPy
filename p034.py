#
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import logging

def is_factorial_num(n, f):
    s = 0
    d = n
    while (d>0):
        s += f[d%10]
        d = d//10
    return s == n

def main(args):
    f= [1]
    for i in range(1,10):
        f.append(f[-1]*i)


    max_f = 2540160
    res = []
    for i in range(10, max_f):
        if (is_factorial_num(i, f)):    
            res.append(i)

    logging.debug(res)
    logging.info(sum(res))
