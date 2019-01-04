#Passcode derivation
# Problem 79 
# A common security method used for online banking is to ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, 
# analyse the file so as to determine the shortest possible secret passcode of unknown length.

import logging

def parse_keylog(filename):
    logs = []
    with open(filename) as f:
        for line in f.readlines():
            logs.append([int(line[x]) for x in range(3)])
    return logs

def main(args):
    logs= parse_keylog("data/p079_keylog.txt")
    logging.debug(logs)

    position = [-1]*10  # init place holder

    for log in logs:
        # a log gives the information of orders of digits
        a, b, c = log
        pa = 0
        if position[a] < pa:
            position[a] = pa
        else:
            pa = position[a]
        pb = pa+1
        if position[b] < pb:
            position[b] = pb
        else:
            pb = position[b]
        pc = pb+1
        if position[c] < pc:
            position[c] = pc
        else:
            pc = position[c]

    logging.debug(position)
    num_digit = 10-position.count(-1)
    n = [0]*num_digit
    for i in range(10):
        p = position[i]
        if p < 0:
            continue
        n[p] = i
    logging.debug(n)

    answer = 0
    for i in range(num_digit):
        answer = answer*10+n[i]
    
    logging.info("answer: {}".format(answer))
