# -*- coding: UTF-8 -*-

#The rules for writing Roman numerals allow for many ways of writing each number (see FAQ: Roman Numerals). However, there is always a "best" way of writing a particular number.
#
#For example, the following represent all of the legitimate ways of writing the number sixteen:
#
#IIIIIIIIIIIIIIII
#VIIIIIIIIIII
#VVIIIIII
#XIIIIII
#VVVI
#XVI
#
#The last example being considered the most efficient, as it uses the least number of numerals.
#
#The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see FAQ for the definitive rules for this problem).
#
#Find the number of characters saved by writing each of these in their minimal form.
#
#Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
import re
import logging

logger = logging.getLogger('p089')

Rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def Rom2Dec(rom):
    lr = rom[0]
    n = Rom[lr]
    for r in rom[1:]:
        d = Rom[r]
        n += d
        if (Rom[lr] < d):
            assert(d == Rom[lr]*5 or d == Rom[lr]*10)
            n -= Rom[lr]*2
        lr = r
    return n

def Dec2Rom(n):
    rom = 'M'*(n//Rom['M'])
    n = n % Rom['M']
    if (n >= Rom['M'] - Rom['C']):
        rom += 'CM'
        n -= Rom['M'] - Rom['C']
    if (n >= Rom['D']):
        rom += 'D'
        n -= Rom['D']
    if (n >= Rom['D'] - Rom['C']):
        rom += 'CD'
        n -= Rom['D'] - Rom['C']
    rom += 'C'*(n//Rom['C'])
    n = n % Rom['C']
    if (n >=  Rom['C'] - Rom['X']):
        rom += 'XC'
        n -= Rom['C'] - Rom['X']
    if (n >= Rom['L']):
        rom += 'L'
        n -= Rom['L']
    if (n >= Rom['L'] - Rom['X']):
        rom += 'XL'
        n -= Rom['L'] - Rom['X']
    rom += 'X'*(n//Rom['X'])
    n = n % Rom['X']
    if (n >= Rom['X'] - Rom['I']):
        rom += 'IX'
        n -= Rom['X'] - Rom['I']
    if (n >= Rom['V']):
        rom += 'V'
        n -= Rom['V']
    if (n >= Rom['V'] - Rom['I']):
        rom += 'IV'
        n -= Rom['V'] - Rom['I']
    rom += 'I'*n
    return rom
    
def main(args):
    saved = 0
    p = re.compile(r"(\w+)")

    with open("data/p089_roman.txt") as f:
        for line in f:
            m = p.match(line)
            o = m.group(1)
            r = Dec2Rom(Rom2Dec(o))
            logger.debug("{} ->  {} : {}".format(o, r, len(o)-len(r)))
            assert(Rom2Dec(o) == Rom2Dec(r))
            assert(len(o) >= len(r))
            saved += len(o)-len(r)
        
    logger.info("answer: {}".format(saved))
