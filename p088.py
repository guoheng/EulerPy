# -*- coding: UTF-8 -*-

#A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
#
#For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
#
#For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
#
#k=2: 4 = 2 × 2 = 2 + 2
#k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
#k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
#k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
#k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
#
#Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.
#
#In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
#
#What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

import logging
from prime import PrimeNumberPool
import time

logger = logging.getLogger('p088')

all_factors = {}
all_factors_sum = {}
prime = PrimeNumberPool()

def Unique2(lists):
    my_list = []
    for l in lists:
        has_l = False
        for m_l in my_list:
            if (m_l == l):
                has_l = True
        if (has_l):
            continue
        my_list.append(l)
    return my_list

def GetFactors(k, m):
    my_factors = []
    if (k in all_factors):
        for factors in all_factors[k]:
            if (factors[0] <= m):
                my_factors.append(factors)
        return my_factors
    
    # expand factors
    prime_factors = []
    for f, n in prime.Factorize(k):
        prime_factors += [f]*n
    
    if (m < prime_factors[-1]):
        return []
    if (len(prime_factors)==1):
        if (m==k):
            all_factors[k] = [prime_factors]
        return [prime_factors]
    
    for f1 in range(prime_factors[-1], k//prime_factors[0]+1):
        if (k % f1 != 0):
            continue
        if (k//f1 < f1):
            my_factors.append([f1, k//f1])
        factors_1 = GetFactors(k//f1, f1)
        if (len(factors_1) > 0):
            my_factors += [[f1]+x for x in factors_1]
            
    if (m==k):
        my_factors.append([k])
    my_factors = Unique2(my_factors)
    if (m==k):
        all_factors[k] = my_factors
    
    return my_factors
    
def find_smallest_product_sum(k):
    '''find the smallest product-sum for a set of size k'''
    # assume a1 <= a2 <= a3 <= ... <= ak,
    # if a1 + a2 + ... + ak = a1 × a2 × ... × ak
    # then a1 + a2 + ... + ak <= k × ak
    # so a1 × a2 × ... × ak <= k × ak

    # first, find a1 + a2 + ... + ak-1 such that a1 × a2 × ... × ak-1 <= k
    # ak-1 range from 2 to k
    my_smallest_product_sum = 2*k
    m0 = 3
    """
    if k % 4 == 1:
        my_smallest_product_sum = 5*(k+3)//4
        m0 = 6
    elif k % 3 == 1:
        my_smallest_product_sum = 4*(k+2)//3
        m0 = 5
    elif k % 2 == 1:
        my_smallest_product_sum = 3*(k+1)//2
        m0 = 4
    """
    for m in range(m0,k):
        for factors_sum in all_factors_sum[m]:
            my_sum = factors_sum+k-1
            if ( my_sum % (m-1)) == 0:
                ak = my_sum//(m-1)
                my_smallest_product_sum = min(my_smallest_product_sum, m*ak)
    return my_smallest_product_sum

# main
def main(args):
    if args.test:
        K = 12
    else:
        K = 12000
    
    all_smallest_product_sum = []
    set_smallest_product_sum = set()

    ts1 = time.time()
    # pre-caculate product of all_factors
    for k in range(2, K+1):
        GetFactors(k, k)
    for k in range(2, K+1):
        all_factors_sum[k] = [sum(x)-len(x) for x in all_factors[k]]
    ts2 = time.time()
    logger.debug("prepare data struct take {} seconds".format(ts2-ts1))

    for k in range(2,K+1):
        my_smallest_product_sum = find_smallest_product_sum(k)
        logger.debug("Smallest product sum for %d: = %d" % (k, my_smallest_product_sum))
        if (my_smallest_product_sum in set_smallest_product_sum):
            continue
        set_smallest_product_sum.add(my_smallest_product_sum)
        all_smallest_product_sum.append(my_smallest_product_sum)

    logger.info("sum of all smallest_product_sum = {}".format(sum(all_smallest_product_sum)))


