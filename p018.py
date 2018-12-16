#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#   3
#  7 5
# 2 4 6
#8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
#Find the maximum total from top to bottom of the triangle below:
#
#                 75
#                95 64
#              17 47 82
#             18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#       99 65 04 28 06 16 70 92
#      41 41 26 56 83 40 80 70 33
#     41 48 72 33 47 32 37 16 94 29
#    53 71 44 65 25 43 91 52 97 51 14
#   70 11 33 28 77 73 17 78 39 68 17 57
#  91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

import logging

class Node:
    def __init__(self, n=0):
        self.num = n
        self.left = 0
        self.right = 0
        self.description = '%d' % n
         
    def MakeLeaf(self):
        big_child = 0
        if (isinstance(self.left, Node)):
            self.left.MakeLeaf()
            big_child = self.left
        if (isinstance(self.right, Node)):
            self.right.MakeLeaf()
            if (isinstance(big_child, Node)):
                if (self.right.num > big_child.num):
                    big_child = self.right
            else :
                big_child = self.right
        if (isinstance(big_child, Node)):
            self.description += ' + ' + big_child.description
            self.num += big_child.num
        self.left = 0
        self.right = 0

def main(args):
    # build the tree

    tree = [[Node(75)],
            [Node(95), Node(64)],
            [Node(17), Node(47), Node(82)],
            [Node(18), Node(35), Node(87), Node(10)],
            [Node(20), Node( 4), Node(82), Node(47), Node(65)],
            [Node(19), Node( 1), Node(23), Node(75), Node( 3), Node(34)],
            [Node(88), Node( 2), Node(77), Node(73), Node( 7), Node(63), Node(67)],
            [Node(99), Node(65), Node(0o4), Node(28), Node( 6), Node(16), Node(70), Node(92)],
            [Node(41), Node(41), Node(26), Node(56), Node(83), Node(40), Node(80), Node(70), Node(33)],
            [Node(41), Node(48), Node(72), Node(33), Node(47), Node(32), Node(37), Node(16), Node(94), Node(29)],
            [Node(53), Node(71), Node(44), Node(65), Node(25), Node(43), Node(91), Node(52), Node(97), Node(51), Node(14)],
            [Node(70), Node(11), Node(33), Node(28), Node(77), Node(73), Node(17), Node(78), Node(39), Node(68), Node(17), Node(57)],
            [Node(91), Node(71), Node(52), Node(38), Node(17), Node(14), Node(91), Node(43), Node(58), Node(50), Node(27), Node(29), Node(48)],
            [Node(63), Node(66), Node(0o4), Node(68), Node(89), Node(53), Node(67), Node(30), Node(73), Node(16), Node(69), Node(87), Node(40), Node(31)],
            [Node(0o4), Node(62), Node(98), Node(27), Node(23), Node( 9), Node(70), Node(98), Node(73), Node(93), Node(38), Node(53), Node(60), Node( 4), Node(23)]
            ]

    for i in range(14):
        for j in range(len(tree[i])):
            tree[i][j].left = tree[i+1][j]
            tree[i][j].right = tree[i+1][j+1]

    top = tree[0][0]
    top.MakeLeaf()
    logging.info("result is {}".format(top.num))
    logging.debug(top.description)

