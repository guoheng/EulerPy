
#Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
#
#However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
#
#Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
#
#NOTE: The first two lines in the file represent the numbers in the example given above

from math import log
import logging
logger = logging.getLogger('p099')

def parse_base_exp(fname):
    base_exp = []
    with open(fname) as f:
        for line in f:
            base_exp.append([int(x) for x in line.split(',')])
    return base_exp

def main(args):
    base_exp = parse_base_exp("data/p099_base_exp.txt")

    max_line = -1
    max_v = 0
    line_num = 0
    for b, e in base_exp:
        line_v = e*log(b)
        if (line_v > max_v):
            max_line = line_num
            max_v = line_v
        line_num += 1

    logger.info("answer: {}".format(max_line))
