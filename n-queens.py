'''
CECS 451: Artificial Intelligence
Assignment 4: N-Queens Solver
'''

import sys
import random
import math

class Encoding:
    
    def __init__(self, encoding):
        self.encoding = encoding
        self.fitness = 0
        self.probability = 0
        
    def get_Fitness(self):
        return self.fitness
    
    def get_Encoding(self):
        return self.encoding
    
    def get_Probability(self):
        return self.probability
    
    def set_Encoding(self, e):
        self.encoding = e
    
    def set_Fitness(self, f):
        self.fitness = f
    
    def set_Probability(self, p):
        self.probability = p


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
    
    encodings = [] #holds all Encoding objects
    
    #generates k  unique encodings and stores them in the encodings list
    for k in  range(numStates): 
        
        generated_encoding_list = random.sample(range(numQueens), numQueens) #generates a list of n unique nums
        encoding_string = ""
    
        for i in generated_encoding_list:
            encoding_string += str(generated_encoding_list[i])
            
        
            
        encodings.append(Encoding(encoding_string))
    
    return encodings

def gen_probabilities(encodings):
    #calculating the probability of selection for each encoding using
    #cost = encoding_i's fitness / summation of fitnesses

    denominator = 0
    
    for e in encodings: 
        f = fitness_func(e.get_Encoding())
        e.set_Fitness(f)
        denominator += f
    
    for e in encodings:
        prob = e.get_Fitness() / denominator 
        e.set_Probability(prob)
        #print(prob)
       
    #sort encodings by decreasing fitness
    sorted_encodings = []
    for i in range(len(encodings)): 
        temp_encoding = max(encodings, key=lambda item: item.probability)  #gets the encoding w/ max prob
        index = encodings.index(temp_encoding)   #gets the index of max 
        del encodings[index] #deletes it from encodings
        sorted_encodings.append(temp_encoding)
        
    return sorted_encodings
        
    
def local_search():
    print('')
    
def selection(numQueens, encodings):
    #implementation of stochastic universal sampling
    
    next_gen = [] #encodings selected for next generation
    num_pointers = math.ceil((numQueens*.75)) #selects .75*numQueens encodings for next population
    point_distance = 1/num_pointers #distance separating each pointer
    start_loc = random.uniform(0, point_distance) #get starting point of 1st pointer
            
    index = 0        
    sum = encodings[index].get_Probability() 
    
    #locates which encoding each pointer is located in
    for i in range(num_pointers): 
        pointer = i*point_distance + start_loc # position of pointer
        if pointer <= sum: #point is located in this encoding
            next_gen.append(encodings[index])
        else:   #need to locate the encoding the pointer is in
            index+=1
            for j in range(index, len(encodings)):
                sum += encodings[j].get_Probability() 
                if pointer <= sum:
                    next_gen.append(encodings[j])
                    break;
            index = j    
    return next_gen
    

    
def crossover(parent1, parent2):
    # parent1 and parent2 is a list 
    #choose random position to cross ( range 0 -parents DNA size)
    cross_point = random.randint(0, len(parent1)-1)
    
    #Make kid from crossing both parent. Slicing(start, stop) stop at stop - 1
    kid1 = parent1[:cross_point] + parent2[cross_point:]
    kid2 = parent2[:cross_point] + parent1[cross_point:]
    
    #return two of the kids DNA after cross
    return kid1, kid2

def mutation(queenStr):
    length = len(queenStr)
    
    randIdx = random.randrange(length + 1) # generates random index to mutate
    
    if randIdx < length + 1: # if it generates index length + 1 then make no mutations
         randVal = random.randrange(1, length) # random value to change to
         newStr = list(queenStr)
         newStr[randIdx] = str(randVal)
         queenStr = "".join(newStr)
    
    return queenStr # return the mutated string
    
def ncr(a, b):
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
    
def fitness_func(queenStr):
    numQ = len(queenStr)
    # calculate the total combinations - ncr numQ & 2
    totalComb = ncr(numQ, 2)
    numAttack = 0
    
    for i in range(numQ):
        for j in range(i+1, numQ):
            # find pairs of attacking queens in same row
            if queenStr[i] == queenStr[j]:
                numAttack += 1
                
            # find pairs of attacking queens in same diagonal
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
    encodings = gen_probabilities(encodings)
    next_gen = selection(numQueens, encodings) #comment this line out when using the testing below
    
    '''
    #for testing purposes
    
    print("probabilities for encodings:")
    for e in encodings:
        print(e.get_Probability())
        
    next_gen = selection(numQueens, encodings)
    print("encodings chosen for next generation")
    for e in next_gen:
        print(e.get_Probability())
    '''    
    
    
#----------MAIN----------
nqueens_solver(sys.argv[1], sys.argv[2])
