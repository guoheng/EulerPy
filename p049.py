
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
#What 12-digit number do you form by concatenating the three terms in this sequence?

import logging
from prime import PrimeNumberPool

def IsPermute(a, b):
    da = set()
    db = set()
    while (a > 0):
        da.add(a%10)
        a = a//10
    while (b > 0):
        db.add(b%10)
        b = b//10
    return da == db

def IsArithSeq3(q):
    if (len(q) == 3):
        if (q[1]-q[0] == q[2] - q[1]):
            return q
        else:
            return 0
    for i in range(len(q)-2):
        for j in range(i+1, len(q)-1):
            for k in range(j+1, len(q)):
                nq = [q[i], q[j], q[k]]
                if (IsArithSeq3(nq)):
                    return nq
    return 0

def main(args):
    prime = PrimeNumberPool()
    for i in range(10000):
        prime.NewPrime()

    prime_num4 = []
    for p in prime.numbers:
        if (p > 1000 and p < 10000):
            prime_num4.append(p)

    pn4_perm = {}
    pn4_ps = set()
    for i in range(len(prime_num4)-1):
        p = prime_num4[i]
        if (p in pn4_ps):
            continue
        for j in range(i+1, len(prime_num4)):
            q = prime_num4[j]
            if (q in pn4_ps):
                continue
            if (IsPermute(p,q)):
                pn4_ps.add(p)
                pn4_ps.add(q)
                if (p in pn4_perm):
                    pn4_perm[p].append(q)
                else:
                    pn4_perm[p] = [p, q]

    for p in list(pn4_perm.keys()):
        ps = pn4_perm[p]
        if (len(ps) < 3):
            continue
        if (IsArithSeq3(ps)):
            logging.info(ps)
            logging.info(IsArithSeq3(ps))
