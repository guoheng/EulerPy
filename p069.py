import logging
from prime import PrimeNumberPool

def Phi(n, prime):
    factors = prime.getPrimeFactor(n)
    cnt = [1]*n
    for p in factors:
        for i in range(n//p):
            cnt[i*p-1] = 0
    return sum(cnt)

def main(args):
    if args.test:
        m = 3000
        max_phi = 1
        max_n = 1
        brute_force = 1
    else:
        m = 1000*1000
        max_phi = 3
        max_n = 6
        brute_force = 0

    prime = PrimeNumberPool(m)

    '''
    A strait forward way is to calculate the product of primes
    '''
    answer = 1
    for p in prime.numbers:
        while answer < m:
            answer *= p
    logging.info("answer:{}".format(answer))
    return 0
    
    max_num_prime_factors = 1
    for n in range(2, m+1):
        if brute_force:
            phi = Phi(n, prime)
        else:
            '''
            Analysis:
            A lower phi happens when the number n has many prime factors
            '''
            factors = prime.getPrimeFactor(n)
            if len(factors) > max_num_prime_factors:
                max_num_prime_factors = len(factors)
                phi = Phi(n, prime)
                logging.debug("{} factors: {}, phi: {}".format(n, factors, phi))
            else:
                continue
        logging.debug("{} phi = {}".format(n, phi))
        if (phi * max_phi < n):
            max_n = n
            max_phi = float(n)/phi
            logging.debug((max_n, max_phi))
    
    logging.info("answer:{}".format(max_n))
