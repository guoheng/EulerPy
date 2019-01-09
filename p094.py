
#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.
#
#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
#
#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

# My solution:
# Heron's Formula for the area of a triangle
# A = sqrt(p(p-a)(p-b)(p-c)) where p is half the perimeter or (a+b+c)/2
# if a=b, c = a+/-1, p = a+(a+/-1)/2
# A = (p-a)*sqrt(p(p-c)) = c/2*sqrt(a^2-c^2/4)
# so a, c/2 is in a group of a Pythagorean triplet
# let a^2-c^2/4 = b^2, then there are 2 possible solutions:
# 1. a = m^2+n^2, c/2 = m^2-n^2, b = 2mn
#    1.a: c = a+1: m^2 = 3 n^2 +1
#    1.b: c = a-1: m^2 = 3 n^2 -1
#        
# 2. a = m^2+n^2, c/2 = 2mn, b = m^2-n^2, 
#    2.a c = a+1: 4mn = m^2+n^2+1
#    2.b c = a-1: 4mn = m^2+n^2-1


from math import sqrt
import logging

logger = logging.getLogger('p094')

def IntTriangleArea(a, c, squares):
    b2 = 4*a*a-c*c
    if b2 in squares:
        a4 = c*b2
        if (a4%4 == 0):
            return a4//4
    return -1

def main(args):

    # test
    # see if we can find a solution for 
    # 2*n*(n+1) = m*(m+1)

    k = 1000
    max_p = k*k*k
    max_m = int(k*sqrt(k))
    perimeters = []

    square = [x*x for x in range(max_m)]

    for m in range(2, max_m):
        if (square[m] > max_p//3): break

        # find m^2 = 3 n^2 +/- 1
        # 1.7*n < m < 1.8*n <==> m/1.8 < n < m/1.7
        for n in range(m*10//18, m*10//17+1):
            a = square[m]+square[n]
            if (a > max_p//3):
                break
            if square[m] == 3*square[n]+1:            
                c = a+1
                logger.debug((a, a, c))
                perimeters.append(2*a+c)
            if square[m] == 3*square[n]-1:
                c = a-1
                logger.debug((a, a, c))
                perimeters.append(2*a+c)
        
        # 4mn = m^2+n^2 +/- 1
        for n in range(m//5, m//3+1):
            a = square[m]+square[n]
            if 4*m*n == a+1:
                c = a+1
                logger.debug((a, a, c))
                perimeters.append(2*a+c)
            if 4*m*n == a-1:
                c = a-1
                logger.debug((a, a, c))
                perimeters.append(2*a+c)
            
    logger.info('sum of perimeters = {}'.format(sum(perimeters)))
