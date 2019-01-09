# -*- coding: UTF-8 -*-

#Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.
#
#A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.
#
#The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).
#
#By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

import re
import logging
import time

logger = logging.getLogger('p096')

class SuDokuNum:
    def __init__(self, num):
        self.num = num
        self.candidate = []
        if (num == 0):
            self.candidate=list(range(1,10))
    
    def copy(self, sn):
        self.num = sn.num
        self.candidate = []
        for c in sn.candidate:
            self.candidate.append(c)

    def set(self, n):
        self.num = n
        self.candidate = []

    def reduce(self, num_set):
        na = []
        for n in self.candidate:
            if (not n in num_set):
                na.append(n)
        self.candidate = na
        if (len(na) == 1):
            self.num = na[0]
    
    def solved(self):
        return self.num != 0
    
    def is_candidate(self, n):
        return n in set(self.candidate)

    def is_invalid(self):
        return self.num==0 and len(self.candidate) == 0
        
def SuDoku_reduce_single(sdk_nums):
    candidates = []
    num_set = set()
    for sn in sdk_nums:
        if sn.solved():
            num_set.add(sn.num)

    for n in range(1,10):
        candidates.append([])
        if (n in num_set): continue
        for sn in sdk_nums:
            if sn.is_candidate(n):
                candidates[n-1].append(sn)
        
    for n in range(1, 10):
        if (len(candidates[n-1]) == 1):
            candidates[n-1][0].set(n)

def SuDoku_reduce_double(sdk_nums):
    for i in range(len(sdk_nums)-1):
        si = sdk_nums[i]
        if (len(si.candidate) == 2):
            dbl = set(si.candidate)
        else:
            continue
        for j in range(i+1, len(sdk_nums)):
            sj = sdk_nums[j]
            if (dbl==set(sj.candidate)):
                for k in range(len(sdk_nums)):
                    if (k == i): continue
                    if (k == j): continue
                    sdk_nums[k].reduce(dbl)
        
class SuDokuSquare:
    def __init__(self, n00, n01, n02, n10, n11, n12, n20, n21, n22):
        self.num = [[SuDokuNum(n00), SuDokuNum(n01), SuDokuNum(n02)], 
                    [SuDokuNum(n10), SuDokuNum(n11), SuDokuNum(n12)],
                    [SuDokuNum(n20), SuDokuNum(n21), SuDokuNum(n22)]]
        # expend the empty space
        self.num_set = set()
        for i in range(3):
            for j in range(3):
                if (self.num[i][j].solved()):
                    self.num_set.add(self.num[i][j].num)
        self.reduce()

    def copy(self, square):
        for i in range(3):
            for j in range(3):
                self.num[i][j].copy(square.num[i][j])
        self.num_set = set(square.num_set)
        
    def reduce(self):
        self.reduce_single()
        self.reduce_double()
        for i in range(3):
            for j in range(3):
                if (not self.num[i][j].solved()):
                    self.num[i][j].reduce(self.num_set)
                if (self.num[i][j].solved()):
                    self.num_set.add(self.num[i][j].num)
    
    def reduce_single(self):
        my_nums = self.num[0]+self.num[1]+self.num[2]
        SuDoku_reduce_single(my_nums)
                        
    def is_solved(self):
        self.reduce()
        return len(self.num_set) == 9

    def num_unsolved(self):
        return 9-len(self.num_set)

    def reduce_double(self):
        my_nums = self.num[0]+self.num[1]+self.num[2]
        SuDoku_reduce_double(my_nums)
    
    def lock_candidate(self, l, row=-1, col=-1):
        assert(row < 0 or col < 0)
        if (row >= 0):
            for rn in self.num[row]:
                rn.reduce(set([l]))
        if (col >= 0):
            for i in range(3):
                self.num[i][col].reduce(set([l]))

    def lock_row(self):
        locked_rows = []
        for l in range(1,10):
            if (l in self.num_set): 
                locked_rows.append([l,-1])
                continue
            l_row = -1
            locked = False
            for r in range(3):
                for sn in self.num[r]:
                    if (l in set(sn.candidate)):
                        if (l_row < 0):
                            l_row = r
                            locked = True
                        else:
                            locked = False
                        break
            if (locked):
                locked_rows.append([l, l_row])
            else:
                locked_rows.append([l,-1])
        return locked_rows
    
    def lock_col(self):
        locked_col = []
        for l in range(1,10):
            if (l in self.num_set): 
                locked_col.append([l,-1])
                continue
            l_col = -1
            locked = False
            for c in range(3):
                for r in range(3):
                    sn = self.num[r][c]
                    if (l in set(sn.candidate)):
                        if (l_col < 0):
                            l_col = c
                            locked = True
                        else:
                            locked = False
                        break
            if (locked):
                locked_col.append([l, l_col])
            else:
                locked_col.append([l,-1])
        return locked_col

    def is_invalid(self):
        for row in self.num:
            for cell in row:
                if (cell.is_invalid()):
                    return True
        return False
        
class SuDokuPuzzle:
    def __init__(self, num=0):
        if (num == 0):
            self.square = [[SuDokuSquare(0,0,0,0,0,0,0,0,0), SuDokuSquare(0,0,0,0,0,0,0,0,0), SuDokuSquare(0,0,0,0,0,0,0,0,0)],
                           [SuDokuSquare(0,0,0,0,0,0,0,0,0), SuDokuSquare(0,0,0,0,0,0,0,0,0), SuDokuSquare(0,0,0,0,0,0,0,0,0)],
                           [SuDokuSquare(0,0,0,0,0,0,0,0,0), SuDokuSquare(0,0,0,0,0,0,0,0,0), SuDokuSquare(0,0,0,0,0,0,0,0,0)]]
            return
        self.square = [[SuDokuSquare(num[0][0],num[0][1],num[0][2],
                                     num[1][0],num[1][1],num[1][2],
                                     num[2][0],num[2][1],num[2][2]),
                        SuDokuSquare(num[0][3],num[0][4],num[0][5],
                                     num[1][3],num[1][4],num[1][5],
                                     num[2][3],num[2][4],num[2][5]),
                        SuDokuSquare(num[0][6],num[0][7],num[0][8],
                                     num[1][6],num[1][7],num[1][8],
                                     num[2][6],num[2][7],num[2][8])],
                       [SuDokuSquare(num[3][0],num[3][1],num[3][2],
                                     num[4][0],num[4][1],num[4][2],
                                     num[5][0],num[5][1],num[5][2]),
                        SuDokuSquare(num[3][3],num[3][4],num[3][5],
                                     num[4][3],num[4][4],num[4][5],
                                     num[5][3],num[5][4],num[5][5]),
                        SuDokuSquare(num[3][6],num[3][7],num[3][8],
                                     num[4][6],num[4][7],num[4][8],
                                     num[5][6],num[5][7],num[5][8])],
                       [SuDokuSquare(num[6][0],num[6][1],num[6][2],
                                     num[7][0],num[7][1],num[7][2],
                                     num[8][0],num[8][1],num[8][2]),
                        SuDokuSquare(num[6][3],num[6][4],num[6][5],
                                     num[7][3],num[7][4],num[7][5],
                                     num[8][3],num[8][4],num[8][5]),
                        SuDokuSquare(num[6][6],num[6][7],num[6][8],
                                     num[7][6],num[7][7],num[7][8],
                                     num[8][6],num[8][7],num[8][8])]]
        self.row_set = []
        self.col_set = []
        for i in range(9):
            self.row_set.append(set())
            self.col_set.append(set())
        self.reduce_square()
        self.reduce_row_col()

    def get_nums(self):
        nums = []
        for i in range(9):
            nums.append(list(range(9)))
        for i in range(3):
            for j in range(3):
                sq = self.square[i][j]
                for k in range(3):
                    for l in range(3):
                        nums[3*i+k][3*j+l] = sq.num[k][l].num
        return nums
    
    def copy(self, puzzle):
        for r in range(3):
            for c in range(3):
                self.square[r][c].copy(puzzle.square[r][c])

    def reduce_row_col(self):
        self.reduce_square()
        for i in range(9):
            row = self.get_row(i)
            for r in row:
                if (r.solved()):
                    self.row_set[i].add(r.num)
                else:
                    r.reduce(self.row_set[i])
                    
            col = self.get_col(i)
            for c in col:
                if (c.solved()):
                    self.col_set[i].add(c.num)
                else:
                    c.reduce(self.col_set[i])
            
            SuDoku_reduce_single(row)
            SuDoku_reduce_single(col)
            SuDoku_reduce_double(row)
            SuDoku_reduce_double(col)

    def get_row(self, idx):
        row = []
        sr = idx % 3
        for square in self.square[idx//3]:
            row += square.num[sr]
        return row
    
    def get_col(self, idx):
        col = []
        col_idx = idx%3
        for i in range(3):
            for j in range(3):
                col.append(self.square[i][idx//3].num[j][col_idx])
        return col
    
    def reduce_square(self):
        for i in range(3):
            for j in range(3):
                self.square[i][j].reduce()
    
    def is_solved(self):
        self.reduce_row_col()
        self.lock_candidate()
        self.reduce_square()
        for i in range(3):
            for j in range(3):
                if (not self.square[i][j].is_solved()):
                    return False
        return True
    
    def num_unresolved(self):
        unresolved = 0
        for i in range(3):
            for j in range(3):
                unresolved += self.square[i][j].num_unsolved()
        return unresolved
    
    def Print(self, enable_debug=0):
        print("--------------------------------------------")
        for i in range(9):
            print([x.num for x in self.get_row(i)])
        if (enable_debug):
            print("Debug:", self.num_unresolved(), " unresolved")
            print("candidate:")
            for i in range(9):
                row = self.get_row(i)
                print([x.candidate for x in row])
            print("square.num_set:")
            for i in range(3):
                for j in range(3):
                    print(self.square[i][j].num_set)
                    
            print("row_set")
            for i in range(9):
                print(self.row_set[i])
            print("col_set")
            for i in range(9):
                print(self.col_set[i])

    def lock_candidate(self):
        self.reduce_square()
        # lock row
        for i in range(3):
            for j in range(3):
                # lock_row
                lock_row = self.square[i][j].lock_row()
                for l in range(1,10):
                    lr = lock_row[l-1]
                    if (lr[1] < 0): continue
                    for k in range(3):
                        if (k == j): continue
                        self.square[i][k].lock_candidate(l, lr[1], -1)
                # lock_col
                lock_col = self.square[i][j].lock_col()
                for l in range(1,10):
                    lc = lock_col[l-1]
                    if (lc[1] < 0): continue
                    for k in range(3):
                        if (k == i): continue
                        self.square[k][j].lock_candidate(l, -1, lc[1])

    def is_invalid(self):
        for row in self.square:
            for cell in row:
                if (cell.is_invalid()):
                    return True
        return False

def Solve(puzzle, enable_debug = 0, max_try = 50):
    if (enable_debug): print("===========================================================")
    if (enable_debug): puzzle.Print(True)
    for i in range(max_try):
        if (puzzle.is_solved()):
            s00 = puzzle.square[0][0]
            n0 = s00.num[0]
            return (n0[0].num*100+n0[1].num*10+n0[2].num, i)
        if (puzzle.is_invalid()):
            return None
    s00 = puzzle.square[0][0]
    n0 = s00.num[0]
    nums = puzzle.get_nums()
    cs = []
    for i in range(3):
        if (n0[i].solved()):
            cs.append([n0[i].num])
        else:
            cs.append(n0[i].candidate)
    if (len(cs[0]) == 1 and len(cs[1]) == 1 and len(cs[1]) == 1):
        return None 
    for c0 in cs[0]:
        nums[0][0] = c0
        for c1 in cs[1]:
            if (c1 == c0): continue
            nums[0][1] = c1
            for c2 in cs[2]:
                if (c2 == c0 or c2 == c1): continue 
                nums[0][2] = c2
                puzzle2 = SuDokuPuzzle(nums)
                solution = Solve(puzzle2)
                if (solution != None):
                    return solution
                
    return None

def parse_sudoku(fname):
    puzzles = []
    num = []
    with open(fname) as f:
        for line in f:
            if (re.match("Grid",line)):
                continue
            line = line.rstrip()
            num.append([int(x) for x in line])
    assert(len(num) % 9 == 0)
    logger.debug("read in {} number lines for {} puzzles".format(len(num), len(num)//9))
    for i in range(len(num)//9):
        puzzles.append(SuDokuPuzzle(num[i*9:i*9+9]))
    return puzzles

def main(args):
    max_tried = 0
    sum3 = 0

    puzzles = parse_sudoku("data/p096_sudoku.txt")
    for puzzle in puzzles:
        (n3, num_tried) = Solve(puzzle)
        logger.debug((n3, num_tried))
        max_tried = max(max_tried, num_tried)
        sum3 += n3

    logger.debug("max tried:{}".format(max_tried))
    logger.info("answer: {}".format(sum3))
