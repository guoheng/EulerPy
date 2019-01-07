# -*- coding: UTF-8 -*-

#In the game, Monopoly, the standard board is set up in the following way:
#GO     A1     CC1     A2     T1     R1     B1     CH1     B2     B3     JAIL
#H2           C1
#T2           U1
#H1           C2
#CH3           C3
#R4           R2
#G3           D1
#CC3           CC2
#G2           D2
#G1           D3
#G2J     F3     U2     F2     F1     R3     E3     E2     CH2     E1     FP
#
#A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
#
#In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.
#
#At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.
#
#    Community Chest (2/16 cards):
#        Advance to GO
#        Go to JAIL
#    Chance (10/16 cards):
#        Advance to GO
#        Go to JAIL
#        Go to C1
#        Go to E3
#        Go to H2
#        Go to R1
#        Go to next R (railway company)
#        Go to next R
#        Go to next U (utility company)
#        Go back 3 squares.
#
#The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
#
#By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
#
#Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.
#
#If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

import logging
import random

#
# global variables
#
num_square = 40
special_squares = {'GO':0, 'JAIL':10, 'G2J':30, 'C1': 11, 'E3': 24, 'H2': 39, 'R1':5}
set_cc = set([2, 17, 33])
set_ch = set([7, 22, 36])
square_railway = [5, 15, 25, 35]
square_util = [12, 18]
cards_cc = list(range(16))
cards_ch = list(range(16))


def RollDice(n, d):
    dices = []
    for i in range(n):
        dices.append(random.randint(1,d))
    return dices

def NextRU(cs, squares):
    for rs in squares:
        if (rs > cs):
            return rs
    return squares[0]

def DrawCC(square):
    my_card = cards_cc.pop(0)
    cards_cc.append(my_card)
    if (my_card == 0): # Advance to GO
        return special_squares['GO']
    if (my_card == 1): # Go to JAIL
        return special_squares['JAIL']
    return square

def DrawCH(square):
    my_card = cards_ch.pop(0)
    cards_ch.append(my_card)
    if (my_card == 0): # Advance to GO
        return special_squares['GO']
    if (my_card == 1): # Go to JAIL
        return special_squares['JAIL']
    if (my_card == 2): # Go to C1
        return special_squares['C1']
    if (my_card == 3): 
        # Go to E3
        return special_squares['E3']
    if (my_card == 4):
        # Go to H2
        return special_squares['H2']
    if (my_card == 5):
        # Go to R1
        return special_squares['R1']
    if (my_card == 6):
        # Go to next R (railway company)
        return NextRU(square, square_railway)
    if (my_card == 7):
        # Go to next R
        return NextRU(square, square_railway)
    if (my_card == 8):
        # Go to next U (utility company)
        return NextRU(square, square_util)
    if (my_card == 9):
        # Go back 3 squares.
        return square-2
    return square


def PlayGame(roll, dice):
    sq_cnt = [0]*num_square
    square = 0
    num_double = 0
    random.shuffle(cards_cc)
    random.shuffle(cards_ch)
    for i in range(roll):
        dices = RollDice(2, dice)
        if (dices[0] == dices[1]):
            num_double += 1
        else:
            num_double = 0
        if (num_double == 3):
            square = special_squares['JAIL']
            num_double = 0
        else:
            step = sum(dices)
            square = (square + step) % num_square
            
        if (square == special_squares['G2J']):
            square = special_squares['JAIL']
        elif (square in set_cc):
            square = DrawCC(square)
        elif (square in set_ch):
            square = DrawCH(square)
            if (square in set_cc):
                square = DrawCC(square)
            
        sq_cnt[square] += 1
    
    return sq_cnt

# sort the square count
def SortIdx(sc):
    sc_idx = {}
    tot = sum(sc)
    for i in range(len(sc)):
        sc_idx[sc[i]] = i
    sc.sort()
    for c in sc:
        logging.debug('''square %d count %d : %f%%''' % (sc_idx[c], c, 100.0*c/tot))
    return (sc_idx[sc[-1]], sc_idx[sc[-2]], sc_idx[sc[-3]])

#
# main
#
def main(args):
    if args.test:
        dice = 6
    else:
        dice = 4

    game = 100
    roll = 100000
    square_count = [0]*num_square

    for g in range(game):
        sqc = PlayGame(roll, dice)
        for i in range(num_square):
            square_count[i] += sqc[i]
            
    logging.debug(square_count)

    largest3 = SortIdx(square_count)
    logging.info("answeer: {}".format(largest3))

