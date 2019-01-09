# -*- coding: UTF-8 -*-

#The points P (x_(1), y_(1)) and Q (x_(2), y_(2)) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
#
#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0 ≤ x_(1), y_(1), x_(2), y_(2) ≤ 2.
#
#Given that 0 ≤ x_(1), y_(1), x_(2), y_(2) ≤ 50, how many right triangles can be formed?

import logging

logger = logging.getLogger('p091')

class Vector:
    '''2D vector'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def minus(self, v):
        return Vector(self.x-v.x, self.y-v.y)
    
    def dot(self, v):
        return self.x*v.x + self.y*v.y
    
    def val(self):
        return (self.x, self.y)
    
def IsRat(v1, v2):
    '''does v1, v2 form a right angle triangle'''
    if (v1.dot(v2) == 0): return 1
    v3 = v1.minus(v2)
    if (v1.dot(v3) == 0): return 1
    if (v2.dot(v3) == 0): return 1
    return 0

def main(args):

    n = 0
    m = 50
    for x1 in range(m):
        for y1 in range(m+1):
            if (x1 == 0 and y1 == 0): continue
            v1 = Vector(x1, y1)
            for x2 in range(x1, m+1):
                for y2 in range(m+1):
                    if (x1 == x2 and y2 <= y1): continue
                    v2 = Vector(x2, y2)
                    n += IsRat(v1, v2)

    logger.info("answer: {}".format(n+m))

