#Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#How many routes are there through a 20x20 grid?

import os,logging

def main(args):
    n = 1
    for i in range(21, 41):
        n = n * i
        
    for i in range(2,21):
        n = n // i
        
    logging.info("result is {}".format(n))

