#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#   3
#  7 5
# 2 4 6
#8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
# a 15K text file containing a triangle with one-hundred rows.

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

def parse_triangle(fname):
    tree = []
    with open(fname) as f:
        for line in f.readlines():
            tree.append([Node(int(x)) for x in line.split()])
    return tree

def main(args):
    # creat the tree
    tree = parse_triangle("data/p067_triangle.txt")

    for i in range(len(tree)-1):
        for j in range(len(tree[i])):
            tree[i][j].left = tree[i+1][j]
            tree[i][j].right = tree[i+1][j+1]

    tree[0][0].MakeLeaf()
    logging.info("answer: {}".format(tree[0][0].num))
    logging.debug(tree[0][0].description)
    