
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number whose proper divisors are less than the number is called deficient and a number whose proper divisors exceed the number is called abundant.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import logging

def d(n):
    res = 1
    for i in range(2, int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            res += i
            if i * i != n:
                res += n//i
    return res

def main(args):
    abundant = [12]

    for i in range(14, 28124):
        if (d(i) > i):
            abundant.append(i)
    
    s = 28124*28125//2

    soa = set()
    for i in abundant:
        for j in abundant:
            if (i + j < 28125):
                soa.add(i+j)

    logging.info(s - sum(soa))

