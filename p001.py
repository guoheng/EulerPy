#

import os,logging

def SumMultiple(cap=1000, a=3, b=5):
    ''' Find multiples of factors

        Parameters
        ----------
        cap : The range of number to search
        a : first factor
        b : second factor
    '''
    mysum = 0
    for i in range(1, cap//a+1):
        mysum += i*a
    for i in range(1, cap//b+1):
        mysum += i*b
    for i in range(1, cap//(a*b)+1):
        mysum -= i*a*b
    return mysum

def main(args):
    description = '''
    Multiples of 3 and 5

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    '''

    if args.verbosity > 1:
        logging.info(description)
    

    if args.test:
        cap = 10
    else:
        cap = 1000

    sum = SumMultiple(cap-1, 3, 5)
    solution = 'sum of all the multiples of 3 or 5 below {} is {}'.format(cap, sum)
    logging.info(solution)
