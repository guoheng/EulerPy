
#The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import logging

def parse_words(fname):
    with open(fname) as f:
        data = f.read()
        words = data.split('''","''')
        # remove begining and end "
        words[0] = words[0][1:]
        words[-1] = words[-1][:-1]
    return words

def val(w, letter):
    s = 0
    for l in w:
        s += letter[l]
    return s

def main(args):
    letter = {}
    tmp = 1
    for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter[l] = tmp
        tmp += 1
        
    triangle_num = set()
    for n in range(1,100):
        triangle_num.add(n*(n+1)/2)
        
    num = 0
    words = parse_words("data/p042_words.txt")
    for w in words:
        if (val(w, letter) in triangle_num):
            num += 1

    logging.info(num)
