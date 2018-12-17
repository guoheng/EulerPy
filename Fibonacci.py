class FibonacciNumber:
    def __init__(self):
        self.numbers = [1, 1]

    def Compute(self, n):
        for i in range(n):
            self.numbers.append(self.numbers[-1]+self.numbers[-2])
