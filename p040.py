import logging

def FindDigit(n, total_digits):
    '''Find the nth digits'''
    i = 0
    #import pdb; pdb.set_trace()
    for d in total_digits:
        i += 1
        logging.debug("FindDigit: i={}, n={}".format(i, n))
        if n <= d:
            number = d//9//i + (n-1)//i
            mydigits = []
            for j in range(i):
                mydigits.append(number%10)
                number = number // 10
            mydigits.reverse()
            return mydigits[n%i-1]
        else:
            n -= d

def main(args):
    description  = '''
    Champernowne's constant
    Problem 40 
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    '''

    if args.test:
        position = [12,15]
    else:
        position = [1]
        for i in range(6):
            position.append(position[-1]*10)

    total_digits = [9]
    # 2-digit number
    for i in range(2,7):
        total_digits.append(i*9*(10**(i-1)))

    logging.debug("total_digits:{}".format(total_digits))
    logging.debug("n:{}".format(position))

    result = 1
    for n in position:
        d = FindDigit(n, total_digits)
        result *= d
        logging.debug("{}-th digit:{}".format(n, d))

    logging.info("solution:{}".format(result))
