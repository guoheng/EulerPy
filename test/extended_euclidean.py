#!/usr/bin/env python

import random

from util import GCD, ExtendedEuclidean
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    for i in range(100):
        a, b = random.randint(10, 1000), random.randint(100, 1000)
        gcd = GCD(a, b)
        logging.info("gcd({},{})={}".format(a, b, gcd))
        x, y = ExtendedEuclidean(a, b)
        logging.info("{}*{}+{}*{}={}".format(x, a, y, b, x*a+y*b))
        assert(x*a+y*b == gcd)

    logging.info("Test passed!")