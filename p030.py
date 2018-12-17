#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
#
#As 1 = 1^4 is not a sum it is not included.
#
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import logging

def is_five_p(n):
    d = []
    n1 = n
    while (n1>0):
        d.append(n1%10)
        n1 = n1//10
    p = 0
    for i in d:
        p += i**5
    return n == p

def main(args):
    sfp = []
    for n in range(20, 395277):
        if (is_five_p(n)):
            sfp.append(n)
            
    logging.debug(sfp)
    logging.info(sum(sfp))
