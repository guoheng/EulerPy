
#By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
#
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
#
#What is the largest square number formed by any member of such a pair?
#
#NOTE: All anagrams formed must be contained in the given text file.

from math import sqrt
from util import Digits
import logging
logger = logging.getLogger('p098')

def parse_words(fname):
    with open(fname) as f:
        line = f.readline()
        return [x.replace('"', '') for x in line.split(',')]

def anagram(a, b):
    sa = set(list(a))
    sb = set(list(b))
    if (len(sa) > 10): return False
    if (len(sb) > 10): return False
    return sa == sb

# global variables
squares = []
max_sq = 1000*1000

def CanBeSquare(x):
    a = 1
    for i in range(len(x)):
        a = a*10
    ia = int(sqrt(a/10))
    ib = int(sqrt(a))
    possible_sq = {}

    if ia > max_sq - 1:
        return possible_sq
    if ib > max_sq - 1:
        ib = max_sq
        
    for i in range(ia, ib):
        [sq, digits_sq] = squares[i]
        if len(digits_sq) < len(x):
            continue
        if len(digits_sq) > len(x):
            break
        set_digit = set(digits_sq)
        set_x = set(list(x))
        if len(set_digit) == len(set_x):
            mydict = {}
            is_sqr = True
            for j in range(len(x)):
                if x[j] in mydict:
                    if (mydict[x[j]] != digits_sq[j]):
                        is_sqr = False
                        break
                else:
                    mydict[x[j]] = digits_sq[j]
            if (is_sqr):
                possible_sq[sq] =digits_sq
    return possible_sq

def FindMatchSquare(possible_sq, a, b):
    match_sq = {}
    sqs = list(possible_sq.keys())
    set_sq = set(sqs)
    for sqa, dsq in possible_sq.items():
        # build the dictionary for the first word 
        dict = {}
        for j in range(len(a)):
            if a[j] in dict:
                assert(dict[a[j]] == dsq[j])
            else:
                dict[a[j]] = dsq[j]
        # find the possible vaue for the 2nd word
        sqb = 0
        for c in b:
            sqb = sqb*10 + dict[c]
        if sqb in set_sq:
             if a in match_sq:
                 match_sq[a].append(sqa)
                 assert(b in match_sq)
                 match_sq[b].append(sqb)
             else:
                 match_sq[a] = [sqa]
                 match_sq[b] = [sqb]
    return match_sq

def main(args):
    words = parse_words("data/p098_words.txt")
    
    # init global variables
    for i in range(1,max_sq+1):
        sq = i*i
        dsq = Digits(sq)
        dsq.reverse()
        squares.append([sq, dsq])

    anagram_words = []
    lwords = []
    for w in words:
        if (len(w)>4):
            lwords.append(w)
    
#    lwords = ['CARE', 'RACE']
    
    for i in range(len(lwords)-1):
        for j in range(i+1,len(lwords)):
            if anagram(lwords[i], lwords[j]):
                anagram_words.append([lwords[i], lwords[j]])
    logger.debug(len(anagram_words))
    
    max_match_sq = 0
    for a, b in anagram_words:
        sqa = CanBeSquare(a)
        if len(sqa) > 0:
            match_sq =  FindMatchSquare(sqa, a, b)
            if (len(match_sq) > 0):
                logger.debug(match_sq)
                for k, v in match_sq.items():
                    max_match_sq = max(max_match_sq, max(v))
    
    logger.info("answer: {}".format(max_match_sq))