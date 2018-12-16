import os,logging

def Collatz(n):
    collatz = [n]
    while (n > 1):
        if (n%2 == 0):
            n = n // 2
        else :
            n = n * 3 + 1    
        collatz.append(n)
        
    return collatz

def main(args):
    description = '''
#The following iterative sequence is defined for the set of positive integers:
#
#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
'''

    r = 1000*1000
    max_len = 1
    max_collatz = []

    for n in range(r//2, r+1):
        collatz = Collatz(n)
        if (max_len < len(collatz)):
            max_collatz = collatz
            max_len = len(collatz)

    logging.debug(max_collatz)
    logging.debug("lenth: {}".format(max_collatz))
    logging.info("result is {}".format(max_collatz[0]))
