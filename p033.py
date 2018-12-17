
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import logging

def main(args):
    den = []
    num = []
    for a in range(1,10):
        for b in range(1,10):
            if (a==b):
                continue
            for c in range(1,10):
                if (10*a*c+b*c == 10*a*b+a*c):
                    if (a > c):
                        (a,c) = (c,a)
                    num.append(a)
                    den.append(c)

    logging.debug(num)
    logging.debug(den)
    n = 1
    d = 1
    for i in range(len(den)):
        n = n*num[i]
        d = d*den[i]

    logging.debug("{}/{}".format(n, d))
    logging.info(d//n)
