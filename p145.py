# -*- coding: UTF-8 -*-

#Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
#There are 120 reversible numbers below one-thousand.
#
#How many reversible numbers are there below one-billion (109)?

from util import Digits
import logging
logger = logging.getLogger('p145')

def ReversibleInt(n):
    if (n%10==0):
        return False
    d = Digits(n)
    return Reversible(d)

def Reversible(d):
    l = len(d)
    c = 0
    for i in range(l):
        s = d[i]+d[l-1-i]+c
        if (s%2 == 0):
            return False
        c = s//10
    return True

def OddPair(c):
    pair = []
    for d1 in range(10):
        for d2 in range(10):
            s = d1+d2+c
            if (s%2 == 0):
                continue
            pair.append([d1,d2])
    return pair

def FindReversible(n):
    '''find the number of revisible < n'''
    num_reversible = 0
    for i in range(1, n):
        if ReversibleInt(i):
            num_reversible += 1
    return num_reversible

def FindReversiblePair2():
    pair4 = []
    pair0 = []
    for d1 in range(1, 10):
        for d2 in range(1, 10):
            s = d1+d2
            if (s%2 == 0):
                continue
            pair0.append([d1,d2])

    for p0 in pair0:
        c = sum(p0)//10
        pair1 = OddPair(c)
        for p1 in pair1:
            pair4.append([p0[0], p1[0], p1[1], p0[1]])
    return pair4

def FindReversible6():
    pair6 = []
    pair0 = []
    for d1 in range(1, 10):
        for d2 in range(1, 10):
            s = d1+d2
            if (s%2 == 0):
                continue
            pair0.append([d1,d2])

    for p0 in pair0:
        c = sum(p0)/10
        pair1 = OddPair(c)
        for p1 in pair1:
            c2 = (sum(p1)+c)//10
            pair2 = OddPair(c2)
            for p2 in pair2:
                pair6.append([p0[0], p1[0], p2[0], p2[1], p1[1], p0[1]])
    return pair6
    
def main(args):

    n = 1000*100

    num_reversible = FindReversible(n//100)
    logger.debug("Totol reversible number below {} is {}".format(n//100, num_reversible))
    num_reversible = FindReversible(n//10)
    logger.debug("Totol reversible number below {} is {}".format(n//10, num_reversible))
    num_reversible = FindReversible(n)
    logger.debug("Totol reversible number below {} is {}".format(n, num_reversible))

    num_reversible4 = num_reversible

    reversible4 = FindReversiblePair2()

    num_reversible5 = 0
    num_reversible6 = 0
    for p4 in reversible4:
        for i in range(10):
            d5 = [p4[0], p4[1],i, p4[2], p4[3]]
            if (Reversible(d5)):
                num_reversible5 += 1
        for i in range(100):
            d6 = [p4[0], p4[1],i//10, i%10, p4[2], p4[3]]
            if (Reversible(d6)):
                num_reversible6 += 1

        
    logger.debug("Totol reversible 5-digital number is {}".format(num_reversible5))
    logger.debug("Totol reversible 6-digital number is {}".format(num_reversible6))

    reversible6 = FindReversible6()

    num_reversible7 = 0
    num_reversible8 = 0
    num_reversible9 = 0
    for p6 in reversible6:
        for i in range(10):
            d7 = p6[:3]+[i]+p6[3:]
            if (Reversible(d7)):
                num_reversible7 += 1

        c = (p6[2]+p6[3])//10
        pair4 = OddPair(c)
        for p4 in pair4:
            d8 = p6[:3]+p4+p6[3:]
            if (Reversible(d8)):
                num_reversible8 += 1
            for i in range(10):
                d9 = d8[:4]+[i]+d8[4:]
                if (Reversible(d9)):
                    num_reversible9 += 1

    logger.debug("Totol reversible 7-digital number is {}".format(num_reversible7))
    logger.debug("Totol reversible 8-digital number is {}".format(num_reversible8))
    tot_reversible8 = num_reversible8+num_reversible7+num_reversible6+num_reversible5+num_reversible4
    logger.debug("Totol reversible number < 10^8 is {}".format(tot_reversible8))
    logger.debug("Totol reversible 9-digital number is {}".format(num_reversible9))
    logger.info("Totol reversible number < 10^9 is {}".format(tot_reversible8+num_reversible9))



