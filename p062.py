
#The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
#Find the smallest cube for which exactly five permutations of its digits are cube.

import logging

def Digits(a):
    da = []
    while (a):
        da.append(a%10)
        a = a//10
    da.sort()
    return da

def IsPermute(a,b):
    return Digits(a) == Digits(b)

def main(args):
    cubes = []
    m = 10000

    for n in range(m):
        cubes.append(n*n*n)

    pcube = {}

    for i in range(m-1):
        for j in range(i+1, m):
            ci = cubes[i]
            cj = cubes[j]
            if (cj > ci*10): break
            if (IsPermute(cubes[i], cubes[j])):
                if (ci in pcube):
                    pcube[ci].append(cj)
                    if (len(pcube[ci])>3):
                        logging.info("answer: {}".format(ci))
                        logging.debug((ci, pcube[ci]))
                        return 0
                else:
                    pcube[ci] = [cj]

    logging.debug(pcube[(345, 41063625)])
    for ci in list(pcube.keys()):
        cj = pcube[ci]
        if (len(cj)>2):
            logging.debug((ci, cj))
