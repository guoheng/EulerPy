
#There are exactly ten ways of selecting three from five, 12345:
#
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#In combinatorics, we use the notation, 5C3 = 10.
#
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
#How many values of  nCr, for 1 <= n <= 100, are greater than one-million?

import logging

def NumCom(n, m):
    c = 1
    for r in range(n//2):
        if (c > m):
            return n+1-r*2
        c = c*(n-r)//(r+1)
    return 0

def main(args):
    m = 1000000
    s = 0
    for n in range(101):
        s += NumCom(n, m)
        
    logging.info(s)
