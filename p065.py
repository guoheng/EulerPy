#
# https://projecteuler.net/problem=65

import logging

def main(args):
    e = [2]

    for k in range(1,40):
        e.append(1)
        e.append(2*k)
        e.append(1)

    k = 100
    e1 = e[:k]
    e1.reverse()

    (n, d) = (0, 1)
    for k in e1:
        (n, d) = (d, n+d*k)

    logging.debug((n, d))

    s = 0
    while (d):
        s += d%10
        d = d//10

    logging.info("answer: {}".format(s))
