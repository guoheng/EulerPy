
#Find the sum of the digits in the number 100!

import logging

def main(args):
    n = 1
    for i in range(2,100):
        n = n*i

    logging.debug(n)
    s = 0
    while (n > 0):
        s += n%10
        n = n // 10
        
    logging.info(s)
