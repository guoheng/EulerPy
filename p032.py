#The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import logging
import permute

def check(p):
    # check aaaa = bbbb x c
    a = p[0]*1000+p[1]*100+p[2]*10+p[3]
    b = p[4]*1000+p[5]*100+p[6]*10+p[7]
    c = p[8]
    if (a==b*c):
        logging.debug("%d = %d x %d" % (a,b,c))
        return a
    # check aaaa = bbb x cc
    b = p[4]*100+p[5]*10+p[6]
    c = p[7]*10+p[8]
    if (a==b*c):
        logging.debug("%d = %d x %d" % (a,b,c))
        return a
    return -1

def main(args):
    m = set()
    for p in permute.all_perms([1,2,3,4,5,6,7,8,9]):
        n = check(p)
        if (n>0):
            m.add(n)

    logging.info(sum(m))