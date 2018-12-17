#
#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
#(Please note that the palindromic number, in either base, may not include leading zeros.)

import logging

def is_palindromic(d):
    for i in range(len(d)//2):
        if (d[i] != d[-1-i]):
            return 0
    return 1
        
def is_palindramic_10(n):
    d = []
    while (n>0):
        d.append(n%10)
        n = n//10
    return is_palindromic(d)

def is_palindramic_2(n):
    d = []
    while (n>0):
        d.append(n%2)
        n = n//2
    return is_palindromic(d)

def main(args):
    if args.test:
        max_n = 1000
    else:
        max_n = 1000000

    palindromic = []
    for n in range(1,max_n):
        if (is_palindramic_10(n) and is_palindramic_2(n)):
            palindromic.append(n)
            
    logging.debug(palindromic)
    logging.info(sum(palindromic))

