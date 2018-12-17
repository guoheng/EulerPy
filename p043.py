
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#    * d2d3d4=406 is divisible by 2
#    * d3d4d5=063 is divisible by 3
#    * d4d5d6=635 is divisible by 5
#    * d5d6d7=357 is divisible by 7
#    * d6d7d8=572 is divisible by 11
#    * d7d8d9=728 is divisible by 13
#    * d8d9d10=289 is divisible by 17
#
#Find the sum of all 0 to 9 pandigital numbers with this property.

import logging
import permute

def check(p):
    return (int(p[1:4]) % 2 == 0) and \
        (int(p[2:5]) % 3 == 0) and \
        (int(p[3:6]) % 5 == 0) and \
        (int(p[4:7]) % 7 == 0) and \
        (int(p[5:8]) % 11 == 0) and \
        (int(p[6:9]) % 13 == 0) and \
        (int(p[7:10]) % 17 == 0)

def main(args):
    s = 0

    for p in permute.all_perms('0123456789'):
        if (check(p)):
            s += int(p)

    logging.info(s)

    