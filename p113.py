# -*- coding: UTF-8 -*-

#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
#As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.
#
#How many numbers below a googol (10100) are not bouncy?

import logging
logger = logging.getLogger('p113')

#
# global variable
#
class Cache:
    def __init__(self, n):
        '''lookup the result from IncreaseNum/DecreaseNum calculation'''
        self.max = max
        self.increase_num = []
        self.decrease_num = [[], []]
        for i in range(n):
            self.increase_num.append([-1]*10)
            self.decrease_num[0].append([-1]*10)
            self.decrease_num[1].append([-1]*10)
        
    def WriteIncrease(self, n, d, val):
        assert(n > 0 and d > 0)
        self.increase_num[n-1][d-1] = val
        
    def WriteDecrease(self, n, d, first, val):
        assert(n > 0)
        if first:
            self.decrease_num[0][n-1][d] = val
        else:
            self.decrease_num[1][n-1][d] = val
        
    def ReadIncrease(self, n, d):
        assert(n > 0 and d > 0)
        return self.increase_num[n-1][d-1]
    
    def ReadDecrease(self, n, d, first=True):
        assert(n > 0)
        if first:
            return self.decrease_num[0][n-1][d]
        else:
            return self.decrease_num[1][n-1][d]
        
lookup = Cache(100)

def IncreaseNum(n, d=1):
    ''' find the total number of increasing number that below 10^n'''
    result = lookup.ReadIncrease(n, d)
    if result > 0:
        return result
    
    if n == 1:
        result = 10-d
        lookup.WriteIncrease(n, d, result)
        return result
    
    result = 0
    for d1 in range(d, 10):
        result += IncreaseNum(n-1, d1)
        
    lookup.WriteIncrease(n, d, result)
    return result

def DecreaseNum(n, d=9, first=True):
    ''' find the total number of decreasing number that below 10^n'''
    result = lookup.ReadDecrease(n, d, first)
    if result > 0:
        return result
    
    result = 0
    if n == 1:
        if first:
            result = d
        else:
            result = d+1
        lookup.WriteDecrease(n, d, first, result)
        return result

    if first:
        d0 = 1
    else:
        d0 = 0
        
    for d1 in range(d0, d+1):
        result += DecreaseNum(n-1, d1, False)
    lookup.WriteDecrease(n, d, first, result)
    return result


#
# test for DecreaseNum
#

def TestDecreaseNum():
    decrease = [9]
    decrease_2 = 0
    for d1 in range(1,10):
        for d0 in range(0,d1+1):
            decrease_2 += 1
    
    decrease.append(decrease_2)
    
    decrease_3 = 0
    for d2 in range(1,10):
        for d1 in range(0,d2+1):
            for d0 in range(0,d1+1):
                decrease_3 += 1
    
    decrease.append(decrease_3)
    
    decrease_4 = 0
    for d3 in range(1,10):
        for d2 in range(0,d3+1):
            for d1 in range(0,d2+1):
                for d0 in range(0,d1+1):
                    decrease_4 += 1
    
    decrease.append(decrease_4)
    
    decrease_5 = 0
    for d4 in range(1,10):
        for d3 in range(d4+1):
            for d2 in range(d3+1):
                for d1 in range(d2+1):
                    for d0 in range(d1+1):
                        decrease_5 += 1
    
    decrease.append(decrease_5)
    
    decrease_6 = 0
    for d5 in range(1,10):
        for d4 in range(d5+1):
            for d3 in range(d4+1):
                for d2 in range(d3+1):
                    for d1 in range(d2+1):
                        for d0 in range(d1+1):
                            decrease_6 += 1
    
    decrease.append(decrease_6)
    
    logger.debug(decrease)
    logger.debug(sum(decrease))
    
    decrease2 = [9]
    for i in range(2,7):
        decrease2.append(DecreaseNum(i))
    
    logger.debug(decrease2)

def TestIncreaseNum():
    inc1 = [9]
    
    inc_2 = 0
    for d1 in range(1,10):
        for d2 in range(d1, 10):
            inc_2 += 1
    inc1.append(inc_2)
    
    inc_3 = 0
    for d1 in range(1,10):
        for d2 in range(d1, 10):
            for d3 in range(d2, 10):
                inc_3 += 1
    inc1.append(inc_3)
    
    inc_4 = 0
    for d1 in range(1,10):
        for d2 in range(d1, 10):
            for d3 in range(d2, 10):
                for d4 in range(d3, 10):
                    inc_4 += 1
    inc1.append(inc_4)
    
    inc_5 = 0
    for d1 in range(1,10):
        for d2 in range(d1, 10):
            for d3 in range(d2, 10):
                for d4 in range(d3, 10):
                    for d5 in range(d4, 10):
                        inc_5 += 1
    inc1.append(inc_5)
    
    inc_6 = 0
    for d1 in range(1,10):
        for d2 in range(d1, 10):
            for d3 in range(d2, 10):
                for d4 in range(d3, 10):
                    for d5 in range(d4, 10):
                        for d6 in range(d5, 10):
                            inc_6 += 1
    inc1.append(inc_6)
    
    logger.debug(inc1)
    print(sum(inc1))

    inc2 = [9]
    for i in range(2,7):
        inc2.append(IncreaseNum(i,1))
    
    logger.debug(inc2)

def NoBouncyNum(n):
    nobouncy = 0
    for i in range(1,n+1):
        nobouncy += IncreaseNum(i,1) + DecreaseNum(i) - 9
    
    return nobouncy

# main
def main(args):
    
    logger.debug("there are only %d numbers below one-million that are not bouncy" % NoBouncyNum(6))
 
    logger.debug("there are only %d numbers below 10^10 that are not bouncy" % NoBouncyNum(10))
    
    logger.info("there are only %d numbers below google(10^100) that are not bouncy" % NoBouncyNum(100))
   
