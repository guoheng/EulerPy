
#A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
#Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import logging

def SumDigits(n):
    s = 0
    while (n):
        s += n % 10
        n = n//10
    return s

def main(args):
    max_sum = 0
    max_ab = ()
    for a in range(2,100):
        if (a % 10 == 0): continue
        p = a
        for b in range(1,98):
            sd = SumDigits(p) 
            if (sd > max_sum): 
                max_sum = sd
                max_ab = (a, b)
            p = p*a
            
    logging.info((max_sum, max_ab))

