
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p < 1000, is the number of solutions maximised?

import logging

def NumSolution(p):
    ns = 0
    for a in range(1,p//3):
        for b in range(a, (p-a)//2):
            c = p - a - b
            if (a*a+b*b == c*c):
                ns += 1
    return ns

def main(args):
    mns = 3
    max_p = 0
    for p in range(3,1000):
        np = NumSolution(p)
        if (mns < np):
            mns = np
            max_p = p
            logging.debug("{} {}".format(p, np))
    logging.info(max_p)