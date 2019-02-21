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


def display_results(numQueens, encoding):
    #populate chessboard with queens
    board = []
    row = []
    encoding_str = encoding.get_Encoding()

    print('encoding string')
    print(encoding_str)
    
    for i in range(numQueens): #i = rows
        queen_col = int(encoding_str[i])
        for j in range(numQueens): #j = columns
            if j == queen_col:
                row.append('X')
            else:
                row.append('-')
        board.append(row)
        row =[]
        
    for i in range(numQueens):
        for j in range(numQueens):
            print(board[i][j], end=' ')
        print('\n')
            
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

    denominator = 0.0001
    
    for e in encodings: 
        f = fitness_func(e.get_Encoding())
        e.set_Fitness(f)
        denominator += f
    
    for e in encodings:
        prob = e.get_Fitness() / denominator 
        e.set_Probability(prob)
        #print(prob)
       
    return sort_encodings(encodings)

def sort_encodings(encodings):  
    #sort encodings by decreasing fitness
    sorted_encodings = []
    for i in range(len(encodings)): 
        temp_encoding = max(encodings, key=lambda item: item.probability)  #gets the encoding w/ max prob
        index = encodings.index(temp_encoding)   #gets the index of max 
        del encodings[index] #deletes it from encodings
        sorted_encodings.append(temp_encoding)
    
    return sorted_encodings
    
def local_search(queenStr): # finds attacking queens
    numQ = len(queenStr)
    numAttack = 0
    
    for i in range(numQ):
        for j in range(i+1, numQ):
            # find pairs of attacking queens in same row
            if queenStr[i] == queenStr[j]:
                numAttack += 1
                
            # find pairs of attacking queens in same diagonal
            if abs(i-j) == abs(int(queenStr[i]) - int(queenStr[j])):
                numAttack += 1
            
            # do not need to count attacking columns because each index in the
            # string is a column, they will never be in the same index/column
                
    return numAttack
    
def selection(numQueens, encodings):
    #implementation of stochastic universal sampling
    
    next_gen = [] #encodings selected for next generation
    num_pointers = math.ceil((numQueens*.75)) #selects .75*numQueens encodings for next population
    point_distance = 1/num_pointers #distance separating each pointer
    start_loc = random.uniform(0, point_distance) #get starting point of 1st pointer
            
    index = 0        
    sum_sel = encodings[index].get_Probability() 
    
    #locates which encoding each pointer is located in
    for i in range(num_pointers): 
        pointer = i*point_distance + start_loc # position of pointer
        if pointer <= sum_sel: #point is located in this encoding
            next_gen.append(encodings[index])
        else:   #need to locate the encoding the pointer is in
            index+=1
            for j in range(index, len(encodings)):
                sum_sel += encodings[j].get_Probability() 
                if pointer <= sum_sel:
                    next_gen.append(encodings[j])
                    break;
            index = j    
    return next_gen
    

    
def crossover(next_gen, numStates):
    crossover_gen = []
 
    for i in range(numStates):
        # parent1 and parent2 is a list from next_gen selection list (selection population)
        parent1 = random.choice(next_gen).get_Encoding()
        parent2 = random.choice(next_gen).get_Encoding()
        
        #choose random position to cross ( range 0 -parents DNA size)
        cross_point = random.randint(0, len(parent1)-1)

        #Slicing(start, stop) stop at stop - 1
        kid1 = parent1[:cross_point] + parent2[cross_point:]
        kid2 = parent2[:cross_point] + parent1[cross_point:]
        
        crossover_gen.append(Encoding(kid1))
        crossover_gen.append(Encoding(kid2))
    
    return crossover_gen

def mutation(encodings):
    mut_gen = []
    for e in encodings: 
        length = len(e.get_Encoding())
        randIdx = random.randrange(length + 1) # generates random index to mutate
        
        if randIdx < length: # if it generates index length + 1 then make no mutations
             randVal = random.randrange(1, length) # random value to change to
             newStr = list(e.get_Encoding())
             newStr[randIdx] = str(randVal)
             e.set_Encoding("".join(newStr))
             
        mut_gen.append(e)
    return mut_gen # return the mutated string
    
def ncr(a, b):
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
    
def fitness_func(queenStr):
    # calculate the total combinations - ncr numQ & 2
    totalComb = ncr(len(queenStr), 2)    
    # subtract and return
    return totalComb - local_search(queenStr)
    
def nqueens_solver(numQ, numS):
    '''
    # print(numQueens, numStates)

    gen_rand_board(numQueens)
    encodings = gen_encodings(numQueens, numStates)
    encodings = gen_probabilities(encodings)
    next_gen = selection(numQueens, encodings) #comment this line out when using the testing below
    display_results(numQueens, next_gen[0])
    
    
    
    '''
    numQ = int(numQ)
    numS = int(numS)
    goal = ncr(numQ, 2)
    
    step = 0
    
    encodings = gen_encodings(numQ, numS)
    goal = ncr(numQ, 2)
    encoding_answer = Encoding("")
    not_found = True; 
    
    while (not_found):
        encodings = gen_probabilities(encodings)
        for e in encodings:
            if e.get_Fitness() == goal:
                encoding_answer = e
                not_found = False
                break;
             
        next_gen = selection(numQ, encodings)
        crossover_gen = crossover(next_gen, numS)
        mut_gen = mutation(crossover_gen) 
        step += 1
        print("Step ", step)
        encodings = mut_gen
    
    #answer = recursive(encodings, step, numQ, numS)
    display_results(numQ, encoding_answer)
    '''
    found = False
    while not found:
        sort = gen_probabilities(encodings)
        if sort[0].get_Fitness() == goal:
            return encodings[0]
        else:
            next_gen = selection(numQ, sort)
            crossover_gen = crossover(next_gen, numS)
            mut_gen = mutation(crossover_gen)
            step += 1
            print("Step ", step)
            encodings = mut_gen
    '''


def recursive(encodings, step, numQ, numS):
    
    encodings = gen_probabilities(encodings)
    goal = ncr(numQ, 2)

    if encodings[0].get_Fitness() == goal:
        return encodings[0]
    else: 
        next_gen = selection(numQ, encodings)
        crossover_gen = crossover(next_gen, numS)
        mut_gen = mutation(crossover_gen)
        step += 1
        print("Step ", step)
        return recursive(mut_gen, step, numQ, numS)
            
    
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

#nqueens_solver(4, 2)   
#----------MAIN----------
nqueens_solver(sys.argv[1], sys.argv[2])
