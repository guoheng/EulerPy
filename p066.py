
#Consider quadratic Diophantine equations of the form:
#
#x^2 - Dy^2 = 1
#
#For example, when D=13, the minimal solution in x is 6492 - 13x1802 = 1.
#
#It can be assumed that there are no solutions in positive integers when D is square.
#
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
#32 - 2x22 = 1
#22 - 3x12 = 1
#92 - 5x42 = 1
#52 - 6x22 = 1
#82 - 7x32 = 1
#
#Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.
#
#Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.
#
# reference: http://mathworld.wolfram.com/PellEquation.html
#

import logging
from math import sqrt

def NextTerm(n, sn, p):
    (a, b) = p
    c = int(b/(sn-a))
    b1 = (n - a*a)//b
    a1 = c*(n-a*a)//b - a
    return [c, (a1,b1)]

def SqrtFraction(n):
    sn = sqrt(n)
    sf = [int(sn)]
    if (n == sf[0]*sf[0]):
        return sf
    pattern = set()
    p = (sf[0], 1)
    while (not p in pattern):
        pattern.add(p)
        [c, p] = NextTerm(n, sn, p)
        sf.append(c)
    return sf

def ConvergeContinueFraction(a):
    a = a + a[1:]
    p = [a[0], a[0]*a[1]+1]
    q = [1, a[1]]
    for n in range(2, len(a)):
        p.append(a[n]*p[n-1]+p[n-2])
        q.append(a[n]*q[n-1]+q[n-2])
    return (p, q)

def IsSqr(n):
    s = int(sqrt(n))
    if (n == s*s): return True
    return False

def FindSolution(d, pq):
    p = pq[0]
    q = pq[1]
    for n in range(len(p)):
        x = p[n]
        y = q[n]
        if (x*x - d*y*y == 1):
            return [x,y]
    return [0,0]

def main(args):
    if args.test:
        m = 20
    else:
        m = 1001

    max_x = [0,0]
    max_d = 0

    for d in range(2, m):
        if (IsSqr(d)): continue
        x = FindSolution(d, ConvergeContinueFraction(SqrtFraction(d)))
        logging.debug((d, x))
        if (x[0] > max_x[0]):
            max_x = x
            max_d = d

    logging.info("answer: d={}, x={}".format(max_d, max_x))




