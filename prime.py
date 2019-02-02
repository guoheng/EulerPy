#!/usr/bin/env python
#
# caculate the prime numbers
import re
from random import randint

class PrimeNumberPool:
    def __init__(self, maxp=1000, load_from = None):
        if load_from is None:
            self.numbers = [2, 3, 5, 7]
            self.FillTo(maxp)
        else:
            self.LoadTxt(load_from)

    def NewPrime(self):
        new_prime = self.numbers[-1] + 2
        while (not self.IsPrime(new_prime)):
            new_prime += 2
        self.numbers.append(new_prime)

    def FillTo(self, maxp):
        while self.numbers[-1] < maxp:
            self.NewPrime()

    def LoadTxt(self, fname):
        numbers = []
        with open(fname) as f:
            for line in f:
                if re.match(r"^\s*#", line):
                    continue
                line = line.rstrip()
                numbers += [int(x) for x in line.split()]
        self.numbers = numbers

    def IsPrime(self, n):
        if n == 1:
            return False
        while (n > self.numbers[-1]*self.numbers[-1]):
            self.NewPrime()
        for p in self.numbers:
            if (p*p > n):
                return True
            if (n % p == 0):
                return False

    def Miller_Rabin(self, n, k=4):
        # return False if n is composite
        # return True if after k loop, n is not composite
        if n % 2 == 0:
            return False
        d = (n-1)//2
        r = 0
        while d % 2 == 0:
            d = d//2
            r += 1
        for i in range(k):
            a = randint(2, n-2)
            x = 1
            for j in range(d):
                x = x*a%n
            if x in [1, n-1]:
                continue
            continue_k = False
            for j in range(r-1):
                x = x*x%n
                if x == n-1:
                    continue_k = True
            if continue_k:
                continue
            return False
        return True

    def Factorize(self, n):
        # fully factorize nuber n
        if n == 1:
            return []
        if self.IsPrime(n):
            return [(n,1)]
        myfactors = []
        for p in self.numbers:
            if p > n//2:
                break
            if n%p == 0:
                cnt = 0
                while (n%p == 0):
                    n = n // p
                    cnt += 1
                myfactors.append((p, cnt))
        if n == 1:
            return myfactors
        return myfactors + self.Factorize(n)

    def getPrimeFactor(self, n):
        myfactors = self.Factorize(n)
        return [x[0] for x in myfactors]

    def getDivisor(self, n):
        assert(n > 0)
        if n == 1:
            return [1]

        divisor = [1]
        myfactors = self.Factorize(n)
        p, q = myfactors[0]
        for i in range(q):
            divisor.append(divisor[-1]*p)
            n = n // p
        if n == 1:
            return divisor
        divisor2 = self.getDivisor(n)
        divisor_set = set(divisor)
        for p in divisor:
            for q in divisor2:
                divisor_set.add(p*q)

        return list(divisor_set)

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
