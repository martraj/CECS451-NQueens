'''
CECS 451: Artificial Intelligence
Assignment 4: N-Queens Solver
'''

import sys
import random

def gen_rand_board(numQueens):
    board = []
    row = []
    for i in range(numQueens):
        for j in range(numQueens):
            row.append('-')
        board.append(row)
    
    for i in range(numQueens):
        r = random.randint(0,4)
        for j in range(numQueens):
            if j == r:
                board[i][j] = 'X'
            print(board[i][j], end=' ')
        print('\n')
            
    
def local_search():
    print('')
    
def selection():
    print('')
    
def crossover():
    print('')
    
def mutation():
    print('')
    
def fitness_func():
    print('')
    
def nqueens_solver(numQ, numS):
    # print(numQueens, numStates)
    numQueens = int(numQ)
    numStates = int(numS)
    gen_rand_board(numQueens)


#----------MAIN----------
nqueens_solver(sys.argv[1], sys.argv[2])