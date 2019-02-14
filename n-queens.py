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
        for j in range(numQueens):
            print(board[i][j], end=' ')
        print('\n')


    
    #populate chessboard with queens NOT DONE YET 
    #for i in range(numQueens):
        #for j in (numQUeens):
            #row[i] = 
            
def gen_encodings(numQueens, numStates):
    
    encodings = [] #holds all encoding strings
    
    #generates k  unique encodings and stores them in encodings
    for k in  range(numStates): 
        
        generated_encoding_list = random.sample(range(numQueens), numQueens) #generates a list of n unique nums
        encoding_string = ""
    
        for i in generated_encoding_list:
            encoding_string += str(generated_encoding_list[i])

        
        encodings.append(encoding_string)
    
    print("encodings")
    print(encodings)
        
        

    
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
    gen_encodings(numQueens, numStates)

#----------MAIN----------
nqueens_solver(sys.argv[1], sys.argv[2])