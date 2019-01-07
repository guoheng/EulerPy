# -*- coding: UTF-8 -*-

#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
#
#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

import logging

def main(args):

    twom = 2000000
    d = twom
    sol = ()
    for m in range(1, 100):
        for n in range(1,100):
            num = m*(m+1)*n*(n+1)/4
            if (abs(num-twom) < d):
                d = abs(num-twom)
                sol = (m,n)

    logging.debug(sol)
    logging.info("answer: {}".format(sol[0]*sol[1]))
