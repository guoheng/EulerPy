
#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

import logging

def pn(n, b):
    m = 1
    for i in range(n):
        m = m * n % b
    return m

def main(args):
    if args.test:
        series_size = 10
    else:
        series_size = 1000

    b = 10**10

    s = 0

    for n in range(1, series_size):
        if (n%10 ==0):
            continue
        s += pn(n, b)
        s = s % b

    logging.info(s)

        