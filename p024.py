import math
import logging

""" Lexicographic permutations
Problem 24 
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 """

def main(args):
    # build factorial
    factorial = [1]
    for i in range(10):
        factorial.append(factorial[-1]*(i+1))
    
    logging.debug(factorial)

    position = 1000*1000

    result = []
    digits = list(range(10))
    for i in range(10):
        idx = position//factorial[9-i]
        next_pos = position % factorial[9-i]
        if next_pos == 0:
            d = digits[idx-1]
            result.append(d)
            digits.pop(idx-1)
            digits.reverse()
            result += digits
            break
        else:
            d = digits[idx]
            result.append(d)
            # remove d from digits
            digits.pop(idx)
            position = next_pos

    logging.info(result)
