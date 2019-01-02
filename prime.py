#!/usr/bin/env python
#
# caculate the prime numbers

class PrimeNumberPool:
    def __init__(self, maxp=1000):
        self.numbers = [2, 3, 5, 7]
        self.FillTo(maxp)

    def NewPrime(self):
        new_prime = self.numbers[-1] + 2
        while (not self.IsPrime(new_prime)):
            new_prime += 2
        self.numbers.append(new_prime)

    def FillTo(self, maxp):
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

    def Factorize(self, n):
        # fully factorize nuber n
        if n == 1:
            return []
        if self.IsPrime(n):
            return [(n,1)]
        myfactors = []
        for p in self.numbers:
            if p > n:
                break
            if n%p == 0:
                cnt = 0
                while (n%p == 0):
                    n = n // p
                    cnt += 1
                myfactors.append((p, cnt))
        return myfactors + self.Factorize(n)

    def getPrimeFactor(self, n):
        myfactors = self.Factorize(n)
        return [x[0] for x in myfactors]

    def ReducedFractions(self, a, b):
        for p in self.getPrimeFactor(a):
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

    def NumberOfPrimes(self):
        return len(self.numbers)

    def GetLargestPrime(self):
        return self.numbers[-1]
