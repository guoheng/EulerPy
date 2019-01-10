# -*- coding: UTF-8 -*-

#Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.
#
#Consider the following two triangles:
#
#A(-340,495), B(-153,-910), C(835,-947)
#
#X(-175,41), Y(-421,-714), Z(574,-645)
#
#It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
#
#Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
#
#NOTE: The first two examples in the file represent the triangles in the example given above.

import logging
logger = logging.getLogger('p102')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def cross_product(self, p):
        assert(isinstance(p, Point))
        return self.x*p.y - self.y*p.x

class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.a = Point(ax, ay)
        self.b = Point(bx, by)
        self.c = Point(cx, cy)
        
    def contains_origin(self):
        d1 = self.a.cross_product(self.b) > 0
        d2 = self.b.cross_product(self.c) > 0
        d3 = self.c.cross_product(self.a) > 0
        return d1 == d2 and d2 == d3

def parse_triangle(fname):
    triangle = []
    with open(fname) as f:
        for line in f:
            a = [int(x) for x in line.split(",")]
            triangle.append(Triangle(a[0], a[1], a[2], a[3], a[4], a[5]))
    return triangle

def main(args):
    triangles = parse_triangle("data/p102_triangles.txt")
    tot_num = 0
    for tr in triangles:
        if (tr.contains_origin()):
            tot_num += 1

    logger.info("answer: {}".format(tot_num))
