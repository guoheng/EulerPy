
#In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
#
#    1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
#
#It is possible to make L2 in the following way:
#
#    1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
#How many different ways can L2 be made using any number of coins?

import logging

def main(args):

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    money = 200

    n = 0

    for p200 in range(money//200+1):
        m1 = money - p200*200
        for p100 in range(m1//100+1):
            m2 = m1 - p100*100
            for p50 in range(m2//50+1):
                m3 = m2 - p50*50
                for p20 in range(m3//20+1):
                    m4 = m3 - p20*20
                    for p10 in range(m4//10+1):
                        m5 = m4 - p10*10
                        for p5 in range(m5//5+1):
                            m6 = m5 - p5*5
                            for p2 in range(m6//2+1):
                                n += 1

    logging.info(n)
