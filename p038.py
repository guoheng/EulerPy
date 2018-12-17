#Take the number 192 and multiply it by each of 1, 2, and 3:
#
#    192 x 1 = 192
#    192 x 2 = 384
#    192 x 3 = 576
#
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import logging

pandigital = set(range(1,10))

def check(l):
    s = set()
    for n in l:
        while (n>0):
            d = n%10
            if (d in s):
                return 0
            s.add(d)
            n = n//10
    return s == pandigital

def catnum(l):
    s = ''
    for i in l:
        s += str(i)
    return int(s)

def main(args):
    rslt = []

    for n in range(1,10):
        pd = [x*n for x in range(1,6)]
        if (check(pd)):
            rslt.append(catnum(pd))

    for n in range(10,100):
        pd = [x*n for x in range(1,5)]
        if (check(pd)):
            rslt.append(catnum(pd))

    for n in range(100,1000):
        pd = [x*n for x in range(1,4)]
        if (check(pd)):
            rslt.append(catnum(pd))

    for n in range(1000,10000):
        pd = [x*n for x in range(1,3)]
        if (check(pd)):
            rslt.append(catnum(pd))

    logging.debug(rslt)
    logging.info(max(rslt))

