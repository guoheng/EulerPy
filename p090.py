# -*- coding: UTF-8 -*-

#Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
#
#For example, the square number 64 could be formed:
#
#In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.
#
#For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
#
#However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.
#
#In determining a distinct arrangement we are interested in the digits on each cube, not the order.
#
#{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
#
#But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
#
#How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

import logging

logger = logging.getLogger('p090')

# find all possible cubes
def AllCube():
    cubes = []
    for d0 in range(5):
        for d1 in range(d0+1, 6):
            for d2 in range(d1+1, 7):
                for d3 in range(d2+1, 8):
                    for d4 in range(d3+1, 9):
                        for d5 in range(d4+1, 10):
                            my_cube = [d0,d1,d2,d3,d4,d5]
                            my_set = set(my_cube)
#                            if (6 in my_set and 9 in my_set):
#                                continue
                            if (6 in my_set):
                                if (not 9 in my_set):
                                    my_cube.append(9)
                            if (9 in my_set):
                                if (not 6 in my_set):
                                    my_cube.append(6)
                            my_cube.sort()
                            cubes.append(my_cube)
    return cubes

square_num = [[0,1], [0,4], [0,9], [1,6], [2,5], [3,6], [4,9], [6,4], [8,1]]

def DisplaySquare(c0, c1):
    s0 = set(c0)
    s1 = set(c1)
    for sq in square_num:
        if (not sq[0] in s0):
            if (not sq[0] in s1):
                return False
            # sq[0] in s1 only
            if (not sq[1] in s0):
                return False
            continue
        # sq[0] in s0
        if (sq[1] in s1):
            continue
        # sq[1] not in s1
        if (not sq[1] in s0):
            return False
        # sq[1] in s0 only
        if (not sq[0] in s1):
            return False
        
    return True

def main(args):

    all_cubes = AllCube()
    logger.debug(all_cubes)

    two_cubes = []
    for c0 in all_cubes:
        for c1 in all_cubes:
            if (c1 < c0):
                continue
            if DisplaySquare(c0, c1):
                two_cubes.append([c0,c1])  

    logger.info("answer: {}".format(len(two_cubes)))


