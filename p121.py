# -*- coding: UTF-8 -*-
# Disc game prize fund
# Problem 121
# A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. 
# After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.
#
# The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.
#
# If the game is played for four turns, the probability of a player winning is exactly 11/120, 
# and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.
#
# Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

from fractions import Fraction
from math import factorial

import logging
logger = logging.getLogger('p121')

def ProbabilityBlue(n, b):
    # inputs:
    #   n: number of draws
    #   b: number of blues at the end
    if b > n:
        return 0
    if b == n:
        return Fraction(1, factorial(n+1))

    if b == 0:
        return Fraction(1, n+1)

    last_red = ProbabilityBlue(n-1, b)
    last_blue = ProbabilityBlue(n-1, b-1)
    return last_red*Fraction(n, n+1) + last_blue*Fraction(1, n+1)

def main(args):

    if args.test:
        num_turns = 4
        logger.debug("Probability: {}".format(ProbabilityBlue(4,4)+ProbabilityBlue(4,3)))
    else:
        num_turns = 15

    prob = 0
    for b in range(num_turns//2+1, num_turns+1):
        p = ProbabilityBlue(num_turns, b)
        logger.debug("Porbability of {} blues in {} turns: {}".format(b, num_turns, p))
        prob += p
    
    logger.debug("Porbability of win in {} turns: {}".format(num_turns, prob))

    answer = int(1/prob)
    logger.info("answer: {}".format(answer))
