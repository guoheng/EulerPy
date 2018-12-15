#!/usr/bin/env python
#
# caculate the prime numbers

class PrimeNumberPool:
    def __init__(self, maxp):
        self.numbers = [2, 3, 5, 7, 11]
        while self.numbers[-1] < maxp:
            self.NewPrime()

    def IsPrime(self, n):
        while (n > self.numbers[-1]*self.numbers[-1]):
            self.NewPrime()
        for p in self.numbers:
            if (p*p > n):
                return True
            if (n % p == 0):
                return False
        
    def NewPrime(self):
        new_prime = self.numbers[-1] + 2
        while (not self.IsPrime(new_prime)):
            new_prime += 2
        self.numbers.append(new_prime)

    def Factorize(self, n):
        if n == 1:
            return []
        if (self.IsPrime(n)):
            return [n]
        myfactors = []
        for p in self.numbers:
            if (n%p == 0):
                myfactors.append(p)
                while (n % p == 0):
                    n = n/p
            if (n == 1):
                return myfactors

    def ReducedFractions(self, a, b):
        for p in self.Factorize(a):
            while (a % p == 0 and b % p == 0):
                a = a/p
                b = b/p
        return (a,b)

    def IsSquare(self, n):
        if (n == 1): return True
        if (self.IsPrime(n)): return False
        for p in self.numbers:
            if (n % p == 0):
                p2 = p*p
                while (n % p2 == 0):
                    n = n/p2
                if (n % p == 0 and n % p2 != 0): 
                    return False
            if (n == 1): 
                return True
            assert(p < n)
        assert(False), 'should never be here'
