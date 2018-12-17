
#What is the first term in the Fibonacci sequence to contain 1000 digits?
import logging
from Fibonacci import FibonacciNumber

def main(args):
    if args.test:
        num_dig = 3
    else:
        num_dig = 1000


    fib = FibonacciNumber()

    b = 10**(num_dig-1)
    while (fib.numbers[-1] < b):
        fib.Compute(1)

    logging.info(len(fib.numbers))

