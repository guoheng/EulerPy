
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in red and is equal to 2427.
#
#    
#131    673    234    103    18
#201    96    342    965    150
#630    803    746    422    111
#537    699    497    121    956
#805    732    524    37    331
#    
#
#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

import logging
from util import parse_matrix

def main(args):
    matrix = parse_matrix("data/p081_matrix.txt")
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0): continue
            if (i == 0):
                matrix[i][j] += matrix[i][j-1]
                continue
            if (j == 0):
                matrix[i][j] += matrix[i-1][j]
                continue
            if (matrix[i-1][j] < matrix[i][j-1]):
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += matrix[i][j-1]

    logging.info("answer: {}".format(matrix[n-1][n-1]))

            
            