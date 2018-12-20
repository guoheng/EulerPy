
#The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
#How many n-digit positive integers exist which are also an nth power?

import logging
from math import *

def main(args):
    s = 0
    for n in range(1,10):
        s += int(log(10)/(log(10)-log(n)))

    logging.info("answer: {}".format(s))

