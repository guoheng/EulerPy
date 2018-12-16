
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import string
import logging

def CountLetter(s):
    s1 = s.replace(' ', '')
    return len(s1)

digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teen = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def Num2Str(n):
    s = ' '
    if (n==0):
        return s
    if (n>999):
        s += digit[n//1000-1] + ' thousand'
        n = n % 1000
        if (n > 0):
            s += ' and '
        return s + Num2Str(n)
    
    if (n > 99):
        s += digit[n//100-1] + ' hundred'
        n = n % 100
        if (n>0):
            s += ' and '
        return s + Num2Str(n)
    if (n > 19):
        s += tens[n//10-2] + ' '
        n = n % 10
        return s + Num2Str(n)
    if (n > 10):
        return teen[n-11]
    return digit[n-1]

def main(args):

    s = 0
    for i in range(1001):
        s += CountLetter(Num2Str(i))
    logging.info("result is {}".format(s))


