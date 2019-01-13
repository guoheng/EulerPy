# Pandigital prime sets
# Problem 118 
# Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, 
# different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.
#
# How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

from prime import PrimeNumberPool
from util import all_perms, Digits
import logging
logger = logging.getLogger('p118')

prime = PrimeNumberPool(9999)

def NumberOfList(mylist):
    # get number from concatenating a list of digits
    n = 0
    for d in mylist:
        n = n*10 + d
    return n

def FindPrime(digits):
    # check if a permutation of digits can be a prime
    myprime = []
    for p in all_perms(digits):
        n = NumberOfList(p)
        if prime.IsPrime(n):
            myprime.append(n)
    return myprime

def PrimeN(n):
    # find n-digits primes
    lo = 10**(n-1)
    hi = 10*lo
    pn = []
    for p in prime.numbers:
        if p < lo:
            continue
        if p > hi:
            break
        pn.append(p)
    return pn

def List_pop(list1, list2):
    # return items in list1 but not in list2
    mylist = []
    for i in list1:
        if i in list2:
            continue
        mylist.append(i)
    return mylist

def main(args):
    digits = list(range(1,10))

    prime2 = PrimeN(2)
    # should remove 11 from prime2
    prime2 = prime2[1:]
    prime3 = []
    for p in PrimeN(3):
        d3 = Digits(p)
        if 0 in d3:
            continue
        if len(set(d3)) < 3:
            continue
        prime3.append(p)
    logger.debug(prime3)
    prime4 = []
    for p in PrimeN(4):
        d4 = Digits(p)
        if 0 in d4:
            continue
        if len(set(d4)) < 4:
            continue
        prime4.append(p)
    logger.debug(prime4)


    p18 = []
    # find 1,8 digit prime set
    for p in [2, 3, 5, 7]:
        mydig = digits.copy()
        mydig.pop(p-1)
        myprime = FindPrime(mydig)
        #logger.debug(myprime)
        for n in myprime:
            p18.append((p, n))

    logger.debug("prime set with 1,8 digit: {}".format(len(p18)))
    logger.debug(p18[10:20])

    # find 1, 1, 7 digit prime set
    p117 = []
    for p in [2, 3, 5]:
        for q in [3, 5, 7]:
            if q <= p:
                continue
            mydig = List_pop(digits, [p,q])
            myprime = FindPrime(mydig)
            #logger.debug(myprime)
            for n in myprime:
                p117.append((p, q, n))

    logger.debug("prime set with 1,1,7 digit: {}".format(len(p117)))
    logger.debug(p117[10:20])

    # find 2,7 digit prime set
    p27 = []
    for p2 in prime2:
        d2 = Digits(p2)
        mydig = List_pop(digits, d2)
        for n in FindPrime(mydig):
            p27.append((p2, n))

    logger.debug("prime set with 2,7 digit: {}".format(len(p27)))
    logger.debug(p27[10:20])

    # find 1, 1, 1, 6 digit prime set
    p1116 = []
    for p in [2, 3]:
        for q in [3, 5]:
            if q <= p:
                continue
            for r in [5, 7]:
                if r <= q:
                    continue
                mydig = List_pop(digits, [p,q,r])
                myprime = FindPrime(mydig)
                #logger.debug(myprime)
                for n in myprime:
                    p1116.append((p, q, r, n))

    logger.debug("prime set with 1,1,1,6 digit: {}".format(len(p1116)))
    logger.debug(p1116[10:20])

    # find 1, 2, 6 digit prime set
    p126 = []
    for p2 in prime2:
        d2 = Digits(p2)
        for q in [2,3,5,7]:
            if q in d2:
                continue
            d3 = d2+[q]
            mydig = List_pop(digits, d3)
            myprime = FindPrime(mydig)
            #logger.debug(myprime)
            for n in myprime:
                p126.append((q, p2, n))
    logger.debug("prime set with 1,2,6 digit: {}".format(len(p126)))
    logger.debug(p126[10:20])

    # find 3, 6 digit prime set
    p36 = []
    for p3 in prime3:
        d3 = Digits(p3)
        mydig = List_pop(digits, d3)
        myprime = FindPrime(mydig)
        for n in myprime:
            p36.append((p3, n))
    logger.debug("prime set with 3,6 digit: {}".format(len(p36)))
    logger.debug(p36[10:20])


    # find 1,1,1,1,5 digit prime set
    p1_5 = []
    mydig = [1,4,6,8,9]
    for n in FindPrime(mydig):
        p1_5.append((2,3,5,7,n))
    logger.debug("prime set with 1,1,1,1,5 digit: {}".format(len(p1_5)))
    logger.debug(p1_5[10:20])

    # find 1,1,2,5 digit prime set
    p1_25 = []
    for p2 in prime2:
        d2 = Digits(p2)
        for q in [2,3,5]:
            if q in d2:
                continue
            for r in [3,5,7]:
                if r <= q:
                    continue
                if r in d2:
                    continue
                d4 = d2+[q,r]
                mydig = List_pop(digits, d4)
                myprime = FindPrime(mydig)
                for n in myprime:
                    p1_25.append((q, r, p2, n))
    logger.debug("prime set with 1,1,2,5 digit: {}".format(len(p1_25)))
    logger.debug(p1_25[10:20])

    # find 2,2,5 digit prime set
    p225 = []
    for p2a in prime2:
        d2a = Digits(p2a)
        for p2b in prime2:
            if p2b <= p2a:
                continue
            d2b = Digits(p2b)
            d4 = list(set(d2a+d2b))
            if len(d4) < 4:
                continue
            mydig = List_pop(digits, d4)
            myprime = FindPrime(mydig)
            for n in myprime:
                p225.append((p2a, p2b, n))
    logger.debug("prime set with 2,2,5 digit: {}".format(len(p225)))
    logger.debug(p225[10:20])

    # find 1,3,5 digit prime set
    p135 = []
    for p3 in prime3:
        d3 = Digits(p3)
        for p in [2,3,5,7]:
            if p in d3:
                continue
            d4 = d3+[p]
            mydig = List_pop(digits, d4)
            myprime = FindPrime(mydig)
            for n in myprime:
                p135.append((p, p3, n))
    logger.debug("prime set with 1,3,5 digit: {}".format(len(p135)))
    logger.debug(p135[10:20])

    # find 4,5 digit prime set
    p45 = []
    for p4 in prime4:
        d4 = Digits(p4)
        mydig = List_pop(digits, d4)
        myprime = FindPrime(mydig)
        for n in myprime:
            p45.append((p4, n))
    logger.debug("prime set with 4,5 digit: {}".format(len(p45)))
    logger.debug(p45[10:20])

    # find 1,1,1,2,4 digit prime set
    p124 = []
    for p4 in prime4:
        d4 = Digits(p4)
        mydig = List_pop(digits, d4)
        for p2 in prime2:
            d2 = Digits(p2)
            d3 = List_pop(mydig, d2)
            if len(d3) != 3:
                continue
            if len(List_pop(d3, [2,3,5,7])) == 0:
                p124.append((d3, p2, p4))
    logger.debug("prime set with 1,1,1,2,4 digit: {}".format(len(p124)))
    logger.debug(p124[10:20])

    # find 1,2,2,4 digit prime set
    p1224 = []
    for p4 in prime4:
        d4 = Digits(p4)
        mydig = List_pop(digits, d4)
        for p2 in prime2:
            d2 = Digits(p2)
            d3 = List_pop(mydig, d2)
            if len(d3) != 3:
                continue
            for p2a in prime2:
                if p2a <= p2:
                    continue
                d2a = Digits(p2a)
                d1 = List_pop(d3, d2a)
                if len(d1) != 1:
                    continue
                if d1[0] in [2,3,5,7]:
                    p1224.append((d1[0], p2, p2a, p4))
    logger.debug("prime set with 1,2,2,4 digit: {}".format(len(p1224)))
    logger.debug(p1224[10:20])

    # find 2,3,4/1134 digit prime set
    p234 = []
    p134 = []
    for p4 in prime4:
        d4 = Digits(p4)
        mydig = List_pop(digits, d4)
        for p3 in prime3:
            d3 = Digits(p3)
            d2 = List_pop(mydig, d3)
            if len(d2) != 2:
                continue
            p2 = d2[0]*10+d2[1]
            if p2 in prime2:
                p234.append((p2, p3, p4))
            p2 = d2[1]*10+d2[0]
            if p2 in prime2:
                p234.append((p2, p3, p4))
            if d2[0] in [2,3,5,7] and d2[1] in [2,3,5,7]:
                p134.append((d2, p3, p4))
    logger.debug("prime set with 2,3,4 digit: {}".format(len(p234)))
    logger.debug("prime set with 1,1,3,4 digit: {}".format(len(p134)))
    logger.debug(p234[10:20])
    logger.debug(p134[10:20])

    # find 1,4,4 digit prime set
    p144 = []
    for p4a in prime4:
        d4 = Digits(p4a)
        mydig = List_pop(digits, d4)
        for p4b in prime4:
            if p4b <= p4a:
                continue
            d4b = Digits(p4b)
            d = List_pop(mydig, d4b)
            if len(d) != 1:
                continue
            if d[0] in [2,3,5,7]:
                p144.append((d[0], p4a, p4b))
    logger.debug("prime set with 1,4,4 digit: {}".format(len(p144)))
    logger.debug(p144[10:20])

    p333 = []
    p1233 = []
    p11133 = []
    for p3a in prime3:
        d3a = Digits(p3a)
        for p3b in prime3:
            if p3b <= p3a:
                continue
            d3b = Digits(p3b)
            if len(set(d3a+d3b)) < 6:
                continue
            # find 3,3,3 digit prime set
            for p3c in prime3:
                if p3c <= p3b:
                    continue
                d3c = Digits(p3c)
                if len(set(d3a+d3b+d3c)) == 9:
                    p333.append((p3a, p3b, p3c))
            # find 1,2,3,3 digit prime set
            for p2 in prime2:
                d2 = Digits(p2)
                mydig = List_pop(digits, d2+d3a+d3b)
                if len(mydig) != 1:
                    continue
                if mydig[0] in [2,3,5,7]:
                    p1233.append((mydig[0], p2, p3a, p3b))
            # find 1,1,1,3,3 digit prime set
            mydig = List_pop(digits, d3a+d3b)
            if len(List_pop(mydig, [2,3,5,7])) == 0:
                p11133.append((mydig, p3a, p3b))

    logger.debug("prime set with 3,3,3 digit: {}".format(len(p333)))
    logger.debug(p333[10:20])
    logger.debug("prime set with 1,2,3,3 digit: {}".format(len(p1233)))
    logger.debug(p1233[10:20])
    logger.debug("prime set with 1,1,1,3,3 digit: {}".format(len(p11133)))
    logger.debug(p11133)

    p2223 = []
    p11223 = []
    p111123 = []
    for p3 in prime3:
        d3 = Digits(p3)
        for p2a in prime2:
            d2a = Digits(p2a)
            mydig = List_pop(digits, d3+d2a)
            if len(mydig) != 4:
                continue
            # check 111123
            if mydig == [2,3,5,7]:
                p111123.append((2,3,5,7,p2a, p3))

            for p2b in prime2:
                if p2b <= p2a:
                    continue
                d2b = Digits(p2b)
                # check 2,2,2,3
                for p2c in prime2:
                    if p2c <= p2b:
                        continue
                    d2c = Digits(p2c)
                    if len(set(d3+d2a+d2b+d2c)) == 9:
                        p2223.append((p2a, p2b, p2c, p3))
                # check 1,1,2,3
                d2c = List_pop(digits, d3+d2a+d2b)
                if len(d2c) != 2:
                    continue
                if d2c[0] in [2,3,5,7] and d2c[1] in [2,3,5,7]:
                    p11223.append((d2c, p2a, p2b, p3))

    logger.debug("prime set with 2,2,2,3 digit: {}".format(len(p2223)))
    logger.debug("prime set with 1,1,2,2,3 digit: {}".format(len(p11223)))
    logger.debug("prime set with 1,1,1,1,2,3 digit: {}".format(len(p111123)))
    logger.debug(p111123)

    p12222 = []
    p111222 = []
    for p2a in prime2:
        d2a = Digits(p2a)
        for p2b in prime2:
            if p2b <= p2a:
                continue
            d2b = Digits(p2b)
            if len(set(d2a+d2b)) != 4:
                continue
            for p2c in prime2:
                if p2c <= p2b:
                    continue
                d2c = Digits(p2c)
                if len(set(d2a+d2b+d2c)) != 6:
                    continue
                mydig = List_pop(digits, d2a+d2b+d2c)
                if len(List_pop(mydig, [2,3,5,7])) == 0:
                    p111222.append((mydig, p2a, p2b, p2c))
                for p2d in prime2:
                    if p2d <= p2c:
                        continue
                    d2d = Digits(p2d)
                    d1 = List_pop(mydig, d2d)
                    if len(d1) != 1:
                        continue
                    if d1[0] in [2,3,5,7]:
                        p12222.append((d1[0], p2a, p2b, p2c, p2d))
    logger.debug(p12222)
    logger.debug(p111222)

    answer = len(p18) + len(p117) + len(p27) + \
        len(p1116) + len(p126) + len(p36) + \
        len(p1_5) + len(p1_25) + len(p225) + len(p135) + len(p45) + \
        len(p124) + len(p1224) + len(p234) + len(p134) + len(p144) + \
        len(p11133) + len(p1233) + len(p333) + \
        len(p2223) + len(p11223) + len(p111123) + \
        len(p111222) + len(p12222)
    
    logger.info("answer: {}".format(answer))
