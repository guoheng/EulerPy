
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?

import logging

def main(args):
    p = 1000
    n = 1 << p
    logging.debug(n)

    s = 0
    while (n > 0):
        s += n % 10
        n = n//10

    logging.info("result is {}".format(s))



