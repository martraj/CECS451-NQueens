'''
CECS 451: Artificial Intelligence
Assignment 4: N-Queens Solver
'''

import sys
import random
import math

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
    
    #generates k  unique encodings and stores them in the encodings list
    for k in  range(numStates): 
        
        generated_encoding_list = random.sample(range(numQueens), numQueens) #generates a list of n unique nums
        encoding_string = ""
    
        for i in generated_encoding_list:
            encoding_string += str(generated_encoding_list[i])

        
        encodings.append(encoding_string)
    
    
    return encodings

def gen_probabilities(fitnesses):
    
    probabilities = []
    denominator = 0
    
    for j in fitnesses: 
        denominator += j
    
    for i in fitnesses:
        percent = i / denominator 
        probabilities.append(percent)
        
    return probabilities

    
def local_search():
    print('')
    
def selection():
    print('')
    
def crossover():
    print('')
    
def mutation():
    print('')
    
def ncr(a, b):
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
    
def fitness_func(queenStr):
    numQ = len(queenStr)
    # calculate the total combinations - ncr numQ & 2
    totalComb = ncr(numQ, 2)
    numAttack = 0
    
    # find pairs of attacking queens in same row
    for i in range(numQ):
        for j in range(i+1, numQ):
            if queenStr[i] == queenStr[j]:
                numAttack += 1
                
    # find pairs of attacking queens in same diagonal
    for i in range(numQ):
        for j in range(i+1, numQ):
            if abs(i-j) == abs(int(queenStr[i]) - int(queenStr[j])):
                numAttack += 1
        
    # note - we don't need to count the number of pairs of attacking queens in
    # the same column, because we will initialize the queens to be in separate
    # columns for each state    
    
    # subtract and return
    return totalComb - numAttack
    
def nqueens_solver(numQ, numS):
    # print(numQueens, numStates)
    numQueens = int(numQ)
    numStates = int(numS)
    gen_rand_board(numQueens)
    encodings = gen_encodings(numQueens, numStates)
    print("encodings")
    print(encodings)
    fitnesses = [24, 23, 20, 11]
    print(gen_probabilities(fitnesses))
    
    
#----------MAIN----------
nqueens_solver(sys.argv[1], sys.argv[2])