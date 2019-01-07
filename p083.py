#!/usr/bin/python
# -*- coding: UTF-8 -*-

#NOTE: This problem is a more challenging version of Problem 81.
#
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in red and is equal to 2297.
#
#    
#131    673    234    103    18
#201    96    342    965    150
#630    803    746    422    111
#537    699    497    121    956
#805    732    524    37    331
#    
#
#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

import logging
from util import parse_matrix

class MinPathSum:
    def __init__(self, x, y, val):
        self.position_x = x
        self.position_y = y
        self.pathcost = val
        self.pathsum = 0
        self.connected = False
        self.up = self
        self.down = self
        self.left = self
        self.right = self
        self.pre = 0
        self.path = '%d'%self.pathcost
        
    def GetNeighbour(self):
        return [self.up, self.right, self.down, self.left]
               
    def Optimize(self):
        for neighbour in self.GetNeighbour():
            assert(isinstance(neighbour, MinPathSum))
            if neighbour.connected:
                if self.connected:
                    if neighbour.pathsum + self.pathcost < self.pathsum:
                        self.pathsum = neighbour.pathsum + self.pathcost
                        self.pre = neighbour.path + '+' + self.path
                        self.path = neighbour.path + '+%d'%self.pathcost
                else:
                    self.pathsum = neighbour.pathsum + self.pathcost
                    self.connected = True
                    self.pre = neighbour
                    self.path = neighbour.path + '+' + self.path
                    

def Connect(mps):
    n = len(mps)
    for i in range(n):
        for j in range(n):
            assert(isinstance(mps[i][j], MinPathSum))
            mps[i][j].Optimize()

def PrintPath(mps):
    n = len(mps)
    min_path_sum = []
    for i in range(n):
        min_path_sum.append([])
        for j in range(n):
            min_path_sum[i].append(mps[i][j].path)
    
    logging.debug(min_path_sum)
    return mps[-1][-1].pathsum

def main(args):
    mtx = parse_matrix("data/p082_matrix.txt")
    n = len(mtx)

    mps = []
    border = MinPathSum(-1,-1,-1)

    for i in range(n):
        mps.append([])
        for j in range(n):
            assert(mtx[i][j]>0)
            mps[i].append(MinPathSum(i, j, mtx[i][j]))
            if i == 0:
                mps[i][j].up = border
            if i == n-1:
                mps[i][j].down = border
            if j == 0:
                mps[i][j].left = border
            if j == n-1:
                mps[i][j].right = border
                
    mps[0][0].connected = True
    mps[0][0].pathsum = mps[0][0].pathcost

    # setup the neighbour for each node
    for i in range(n):
        for j in range(n):
            if i > 0:
                mps[i][j].up = mps[i-1][j]
            if i < n-1:
                mps[i][j].down = mps[i+1][j]
            if j > 0:
                mps[i][j].left = mps[i][j-1]
            if j < n-1:
                mps[i][j].right = mps[i][j+1]
                
    # start connect the path
    for i in range(n):
        Connect(mps)

    logging.info("answer: {}".format(PrintPath(mps)))


        
