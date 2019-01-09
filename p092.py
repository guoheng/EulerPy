
#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
#For example,
#
#44 -> 32 -> 13 -> 10 -> 1 -> 1
#85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
#How many starting numbers below ten million will arrive at 89?

import logging

logger = logging.getLogger('p092')

sn1 = set([44, 32, 13, 10, 1])
sn89 = set([85, 89, 145, 42, 2, 20, 4, 16, 37, 58])

def SquareNum(n):
    s = 0
    while (n):
        d = n%10
        s += d*d
        n = n // 10
    if (s in sn1):
        return 1
    if (s in sn89):
        return 89
    if (SquareNum(s) == 1):
        sn1.add(s)
        return 1
    sn89.add(s)
    return 89

def main(args):

    m = 1000*1000*10

    s = 0
    for n in range(2, m):
        if (SquareNum(n) == 89):
            s += 1

    logger.info("answer:{}".format(s))
