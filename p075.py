# -*- coding: UTF-8 -*-

#It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
#
#12 cm: (3,4,5)
#24 cm: (6,8,10)
#30 cm: (5,12,13)
#36 cm: (9,12,15)
#40 cm: (8,15,17)
#48 cm: (12,16,20)
#
#In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
#120 cm: (30,40,50), (20,48,52), (24,45,51)
#
#Given that L is the length of the wire, for how many values of L ≤ 2,000,000 can exactly one integer sided right angle triangle be formed?

import logging
from math import sqrt

one = set()
more = set()
tri_set = set()
b_triangles = []
b_one = set()
b_more = set()

def tri2str(tri):
    tri.sort()
    return "%d,%d,%d" % tuple(tri)

def BentRT(L):
    for a in range(3, L//3):
        for b in range(L//2-a+1, (L-a)//2+1):
            if (b < a): continue
            c = L - a - b
            if (a*a+b*b == c*c):
                b_triangles.append([a,b,c])
                l = a+b+c
                if (l in b_more): continue
                if (l in b_one):
                    b_one.discard(l)
                    b_more.add(l)
                else:
                    b_one.add(l)
                    
def PythagoreanTriple(L):
    '''find primitive Pythagorean triples'''
    triangles = []
    M = int(sqrt(L/2))+1
    for n in range(1,M):
        for m in range(n+1, M+1):
            l = 2*m*(m+n)
            if (l > L): continue
            tri = [m*m-n*n,2*m*n,m*m+n*n]
            str = tri2str(tri)
            if (str in tri_set):
                continue
            triangles.append(tri)
            tri_set.add(str)
    return triangles

def main(args):
    if args.test:
        L = 200
    else:
        L = 1500*1000

    triangles = PythagoreanTriple(L)

    #print triangles
    new_tri = []
    for tri in triangles:
        l = tri[0]+tri[1]+tri[2]
        for n in range(2, L//l+1):
            ntri = [x*n for x in tri]
            nstr = tri2str(ntri)
            if (nstr in tri_set): continue
            tri_set.add(nstr)
            new_tri.append(ntri)

    triangles += new_tri

    for tri in triangles:
        l = tri[0]+tri[1]+tri[2]
        if (l in more): continue
        if (l in one):
            one.discard(l)
            more.add(l)
        else:
            one.add(l)
            
    logging.info("answer:{}".format(len(one)))
    logging.debug(len(more))

