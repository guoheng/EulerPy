#!/usr/bin/env python
#

import argparse,logging
import pickle
from prime import PrimeNumberPool

def save_txt(fname, numbers):
    with open(fname, 'w') as f:
        for n in numbers:
            f.write(str(n))
            f.write("\n")

def save_pkl(fname, numbers):
    with open(fname, 'wb') as f:
        pickle.dump(numbers, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute prime numbers")
    parser.add_argument("-m", "--max", type=int, default=1000000, help="the max limit")
    parser.add_argument("--format", type=str, choices=['pkl', 'txt'], default='pkl', help="save to pkl or txt format")
    parser.add_argument("--save", type=str, required=True, help="file to save the prime numbers")
    parser.add_argument('-v', '--verbosity', type=int, default=0, help='verbosity level for debug')
    args = parser.parse_args()

    if args.verbosity > 0:
        logging.info(args)

    primes = PrimeNumberPool(args.max)
    if args.format == 'pkl':
        save_pkl(args.save, primes.numbers)
    else:
        save_txt(args.save, primes.numbers)
