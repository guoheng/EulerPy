#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
#If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#It can be seen that there are 3 fractions between 1/3 and 1/2.
#
#How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 10,000?

import logging

from prime import PrimeNumberPool

def HCF(n, pd):
    for p in pd:
        if (n % p == 0):
            return 0
    return 1

def main(args):
    if args.test:
        m = 8+1
    else:
        m = 1000*12+1

    prime = PrimeNumberPool(m//2)

    num = 0
    for d in range(3, m):
        d1 = d//2 + 1

        pd = prime.getPrimeFactor(d)
        for n in range(d//3+1, d1):
            if (HCF(n,pd)):
                logging.debug("{}/{}".format(n, d))
                num += 1

    logging.info("answer: {}".format(num))
