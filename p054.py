
#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
#    * High Card: Highest value card.
#    * One Pair: Two cards of the same value.
#    * Two Pairs: Two different pairs.
#    * Three of a Kind: Three cards of the same value.
#    * Straight: All cards are consecutive values.
#    * Flush: All cards of the same suit.
#    * Full House: Three of a kind and a pair.
#    * Four of a Kind: Four cards of the same value.
#    * Straight Flush: All cards are consecutive values of same suit.
#    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
#
#Consider the following four hands dealt to two players:
#Hand         Player 1         Player 2         Winner
#1         5H 5C 6S 7S KD
#Pair of Fives
#         2C 3S 8S 8D TD
#Pair of Eights
#         Player 2
#2         5D 8C 9S JS AC
#Highest card Ace
#         2C 5C 7D 8S QH
#Highest card Queen
#         Player 1
#3         2D 9C AS AH AC
#Three Aces
#         3D 6D 7D TD QD
#Flush with Diamonds
#         Player 2
#4         4D 6S 9H QH QC
#Pair of Queens
#Highest card Nine
#         3D 6D 7H QD QS
#Pair of Queens
#Highest card Seven
#         Player 1
#5         2H 2D 4C 4D 4S
#Full House
#With Three Fours
#         3C 3D 3S 9S 9D
#Full House
#with Three Threes
#         Player 1
#
#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are player one's cards and the last five are player two's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#
#How many hands does player one win?

import logging
import re

class Card:
    '''A card'''
    def __init__(self, vs):
        self.card_val = {'T':10, 'J':11, 'Q':12, 'K': 13, 'A':14}
        self.name = vs
        self.suit = vs[1]
        if (re.match(r"\d", vs[0])):
            self.value = int(vs[0])
        else:
            self.value = self.card_val[vs[0]]
    
    def cmp(self, c):
        return self.value - c.value

class Hand:
    '''A hand of Cards'''
    def __init__(self, cvs):
        self.hand_rank = {"High Card":1, "One Pair" : 2, "Two Pairs" : 3, 
             "Three of a Kind" : 4, "Straight" : 5, "Flush" : 6,
             "Full House" : 7, "Four of a Kind" : 8,
             "Straight Flush" : 9, "Royal Flush" : 10}
        self.cards = []
        for vs in cvs:
            self.cards.append(Card(vs))
        self.cards.sort(key=lambda x: x.value)
        self.suit = set()
        self.value = {}
        for c in self.cards:
            self.suit.add(c.suit)
            if (c.value in self.value):
                self.value[c.value] += 1
            else:
                self.value[c.value] = 1

        if (len(self.value) == 2):
            # identify Four of a Kind or Full House
            for k in list(self.value.keys()):
                if (self.value[k] == 4):
                    self.rank_name = "Four of a Kind"
                    self.rank_value = (self.hand_rank[self.rank_name], k)
                if (self.value[k] == 3):
                    self.rank_name = "Full House"
                    self.rank_value = (self.hand_rank[self.rank_name], k)

        if (len(self.value) == 3):
            pair_values = []
            for k in list(self.value.keys()):
                if (self.value[k] == 3):
                    self.rank_name = "Three of a Kind"
                    self.rank_value = (self.hand_rank[self.rank_name], k)
                if (self.value[k] == 2):
                    self.rank_name = "Two Pairs"
                    pair_values.append(k)
                if (self.value[k] == 1):
                    one_v = k
            if (self.rank_name == "Two Pairs"):
                pair_values.sort()
                pair_values.reverse()
                pair_values.append(one_v)
                self.rank_value = (self.hand_rank[self.rank_name], pair_values)
                
        if (len(self.value) == 4):
            self.rank_name = "One Pair"
            one_values = []
            for k in list(self.value.keys()):
                if (self.value[k] == 2):
                    pair_v = k
                else:
                    one_values.append(k)
            one_values.sort()
            one_values.reverse()
            one_values.insert(0, pair_v)
            self.rank_value = (self.hand_rank[self.rank_name], one_values)
        
        if (len(self.value) == 5):
            values = list(self.value.keys())
            values.sort()
            # identify flush
            if (len(self.suit) == 1):
                self.rank_name = "Flush"
                if (values[0]+4 == values[4]):
                    self.rank_name = "Straight Flush"
                    if (values[0] == 10):
                        self.rank_name = "Royal Flush"
                self.rank_value = (self.hand_rank[self.rank_name], values[4])
            else:
                if (values[0]+4 == values[4]):
                    self.rank_name = "Straight"
                    self.rank_value = (self.hand_rank[self.rank_name], values[4])
                else:
                    self.rank_name = "High Card"
                    values.reverse()
                    self.rank_value = (self.hand_rank[self.rank_name], values)
                    
    def Name(self):
        return "%s : %s" % (self.rank_name, str(self.rank_value))
    
    def Win(self, h):
        rank1, value1 = self.rank_value
        rank2, value2 = h.rank_value            
        return rank1 > rank2 or (rank1==rank2 and value1 > value2)

def parse_hand(fname):
    hands = []
    with open(fname) as f:
        for line in f.readlines():
            cs = line.split()
            if (len(cs) != 10): 
                continue
            h1 = Hand(cs[:5])
            h2 = Hand(cs[5:])
            hands.append((h1, h2))
    return hands

def main(args):
    if args.test:
        h1 = Hand("5H 5C 6S 7S KD".split(" "))
        h2 = Hand("2C 3S 8S 8D TD".split(" "))
        logging.debug(h1.Name())
        logging.debug(h2.Name())
        logging.debug(h1.Win(h2))
        
        h1 = Hand("5D 8C 9S JS AC".split(" "))
        h2 = Hand("2C 5C 7D 8S QH".split(" "))
        logging.debug(h1.Name())
        logging.debug(h2.Name())
        logging.debug(h1.Win(h2))
        
        h1 = Hand("2D 9C AS AH AC".split(" "))
        h2 = Hand("3D 6D 7D TD QD".split(" "))
        logging.debug(h1.Name())
        logging.debug(h2.Name())
        logging.debug(h1.Win(h2))
        
        h1 = Hand("4D 6S 9H QH QC".split(" "))
        h2 = Hand("3D 6D 7H QD QS".split(" "))
        logging.debug(h1.Name())
        logging.debug(h2.Name())
        logging.debug(h1.Win(h2))
        
        h1 = Hand("2H 2D 4C 4D 4S".split(" "))
        h2 = Hand("3C 3D 3S 9S 9D".split(" "))
        logging.debug(h1.Name())
        logging.debug(h2.Name())
        logging.debug(h1.Win(h2))

    else:
        hands = parse_hand("data/p054_poker.txt")
        logging.debug("total {} hands".format(len(hands)))
        h1win = 0
        for h1, h2 in hands:
            if (h1.Win(h2)):
                h1win += 1
        logging.info(h1win)
