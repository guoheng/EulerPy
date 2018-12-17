
#Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
#What is the total of all the name scores in the file?

import logging

def parse_names(fname):
    with open(fname) as f:
        data = f.read()
        names = data.split('''","''')
        # remove begining and end "
        names[0] = names[0][1:]
        names[-1] = names[-1][:-1]
    return names

def score(str, lscore):
    s = 0
    for i in range(len(str)):
        s += lscore[str[i]]
    return s

def main(args):
    names = parse_names("data/p022_names.txt")
    names.sort()

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lscore = {}
    for i in range(1,27):
        lscore[letters[i-1]] = i

    s = 0
    for i in range(len(names)):
        s += score(names[i], lscore)*(i+1)

    logging.info(s)

