
#By replacing the 1st digit of *57, it turns out that six of the possible values: 157, 257, 457, 557, 757, and 857, are all prime.
#
#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import logging
from prime import PrimeNumberPool

def replacing1(s):
    if (len(s) == 1):
        return [s, '*']
    s1 = replacing1(s[1:])
    return [s[0] + x for x in s1] + ['*' + x for x in s1]

def replacing(s):
    rs = []
    rs1 = replacing1(s)
    for r1 in rs1:
        ds = set()
        for i in range(len(s)):
            if (s[i] != r1[i]):
                ds.add(s[i])
        if (len(ds) == 1):
            rs.append(r1)
    return rs

def Bucketize(n, bucket):
    d = str(n)
    st = replacing(d)
    mb = 0
    for s in st:
        if (s in bucket):
            bucket[s].append(n)
            if (mb < len(bucket[s])):
                mb = len(bucket[s])
        else:
            bucket[s] = [n]
            if (mb < 1):
                mb = 1
    return mb

def main(args):
    if args.test:
        mp = 1000
    else:
        mp = 1000000

    prime = PrimeNumberPool(mp)

    bucket = {}

    for p in prime.numbers:
        Bucketize(p, bucket)

    for s in list(bucket.keys()):
        if (len(bucket[s]) == 8):
            logging.debug((s, bucket[s]))
            logging.info("solution: {}".format(bucket[s][0]))