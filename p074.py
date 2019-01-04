
#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
#1! + 4! + 5! = 1 + 24 + 120 = 145
#
#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
#
#169 -> 363601 -> 1454 -> 169
#871 -> 45361 -> 871
#872 -> 45362 -> 872
#
#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
#69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
#78 -> 45360 -> 871 -> 45361 (-> 871)
#540 -> 145 (-> 145)
#
#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

import logging

factorial_set = [1, 1]

def Factorial(n):
    if len(factorial_set) > n:
        return factorial_set[n]
    for i in range(len(factorial_set), n+1):
        factorial_set.append(i*factorial_set[-1])
    return factorial_set[n]

def SumFact(n):
    s = 0
    while (n):
        s += factorial_set[n%10]
        n = n//10
    return s

def ChainSumFact(n):
    lsf = set([n])
    n = SumFact(n)
    while (not n in lsf):
        lsf.add(n)
        n = SumFact(n)
    return lsf

def main(args):
    if args.test:
        num_loop = 200
    else:
        num_loop = 1000000

    sf60 = []
    Factorial(10)
    logging.debug("Factorials: {}".format(factorial_set))

    fmt = "chain of {}: {}"
    if args.test:
        # test SumFact
        for n in [145, 169, 871, 872, 69]:
            chain = ChainSumFact(n)
            logging.debug(fmt.format(n, chain))

    for n in range(num_loop):
        chain = ChainSumFact(n)
        if (len(chain) == 60):
            logging.debug(fmt.format(n, chain))
            sf60.append(n)

    logging.debug(sf60)
    logging.info("answer: {}".format(len(sf60)))
