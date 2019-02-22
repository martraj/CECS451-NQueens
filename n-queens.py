'''
CECS 451: Artificial Intelligence
Assignment 4: N-Queens Solver
'''
import sys
import random
import math
import matplotlib.pyplot as plt
import statistics

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
    num_pointers = math.floor((numQueens*.75)) #selects .75*numQueens encodings for next population
    #print("number of pointers")
    #print(num_pointers)
    point_distance = 1/num_pointers #distance separating each psointer
    #print("distance between pointers")
    #print(point_distance)
    start_loc = random.uniform(0, point_distance) #get starting point of 1st pointer
    #print("start location")
    #print(start_loc)        
    index = 0        
    sum_sel = encodings[index].get_Probability() 
    #print("starting sum first prob")
    #print(sum_sel)
    
    #locates which encoding each pointer is located in
    for i in range(num_pointers): 
        pointer = i*point_distance + start_loc # position of pointer
        #print("pointer " + str(i) + "i s at pos: " + str(pointer))
        if pointer <= sum_sel: #point is located in this encoding
            next_gen.append(encodings[index])
            #print("encoding used")
            #print(encodings[index].get_Encoding())
        else:   #need to locate the encoding the pointer is in
            index+=1
            for j in range(index, len(encodings)):
                sum_sel += encodings[j].get_Probability() 
                #print("current position of sum")
                #print (sum_sel)
                if pointer <= sum_sel:
                    #print("encoding selected ")
                    #print(encodings[j].get_Encoding())
                    next_gen.append(encodings[j])
                    break;
            index = j  
    '''
    print("selected encodings")
    for e in next_gen:
        print(e.get_Encoding())
    '''
    if sum_sel == 0: 
        return encodings
    return next_gen
    

    
def crossover(next_gen, numStates):
    crossover_gen = []
    
    while(len(crossover_gen) < numStates):
        # parent1 and parent2 is a list from next_gen selection list (selection population)
        parent1 = random.choice(next_gen).get_Encoding()
        parent2 = random.choice(next_gen).get_Encoding()
        #print("Crossing {} & {}".format(parent1, parent2))
        #choose random position to cross ( range 0 -parents DNA size)
        cross_point = random.randint(0, len(parent1)-1)
        #Slicing(start, stop) stop at stop - 1
        kid1 = parent1[:cross_point] + parent2[cross_point:]
        kid2 = parent2[:cross_point] + parent1[cross_point:]
        
        if (len(crossover_gen) + 1 == numStates):
            crossover_gen.append(Encoding(kid1)    
        else: 
            crossover_gen.append(Encoding(kid1))
            crossover_gen.append(Encoding(kid2)) 
                                 
    return crossover_gen

def mutation(encodings):
    mut_gen = []
    for e in encodings:
        length = len(e.get_Encoding())
        rand1 = random.randrange(length)
        rand2 = random.randrange(length)
        
        #print("swap at idx {} & idx {}".format(rand1, rand2)
        newStr = list(e.get_Encoding())
        temp = newStr[rand1]
        newStr[rand1] = newStr[rand2]
        newStr[rand2] = temp
        uniqueStr = []
        
        for i in range(len(newStr)):
            if newStr[i] not in uniqueStr:
                uniqueStr.append(newStr[i])
            else:
                r = random.randrange(length)
                while(str(r) in uniqueStr):
                    r = random.randrange(length)
                uniqueStr.append(str(r))
          
        e.set_Encoding("".join(uniqueStr))
        mut_gen.append(e)
        
    return mut_gen # return the mutated string
    
def ncr(a, b):
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
    
def fitness_func(queenStr):
    # calculate the total combinations - ncr numQ & 2
    totalComb = ncr(len(queenStr), 2)    
    # subtract and return
    return totalComb - local_search(queenStr)

def calculate_stats(steps):
    steps = [1,2,4,4,5]
    sorted_steps = sorted(steps)
    sum_steps = sum(steps)
    len_steps = len(steps)
    average = sum_steps/len_steps
    median = statistics.median(steps)
    minimum = min(steps)
    maximum = max(steps)
    
    print("Average: ", average)
    print("Median: ", median)
    print("minimum: ", minimum)
    print("maximum: ", maximum)
    
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
    steps = []
    step = 0
    
    encodings = gen_encodings(numQ, numS)
    goal = ncr(numQ, 2)
    encoding_answer = Encoding("")
    not_found = True; 
                                 
    print("current encodings")                       
    for e in encodings: 
        print (e.get_Encoding())
                                 
    i = 0
    while i<100:
        encodings = gen_probabilities(encodings)
        '''
        print("Goal: ", goal)
        for e in encodings:
            print("{} Fitness: {}".format(e.get_Encoding(), e.get_Fitness()))
        ''' 
            #print("fitness for encoding " + str(e.get_Encoding()) + "is " + str(e.get_Fitness()))
        if (encodings[0].get_Fitness() == goal):
            encoding_answer = encodings[0]
            not_found = False
            break
        next_gen = selection(numQ, encodings)
        
        '''
        print("fittest parent encodings")
        for e in next_gen: 
            print (e.get_Encoding())
        '''
           
        crossover_gen = crossover(next_gen, numS)
        
        '''
        print("crossover encodings")
        for e in crossover_gen: 
            print (e.get_Encoding())
        '''
        
        mut_gen = mutation(crossover_gen) 
        
        '''
        print("mutated parent encodings")
        for e in mut_gen: 
            print (e.get_Encoding())
        '''
        
        step += 1
        print("Step ", step)
        print()
        encodings = mut_gen
        i+=1
    
    #encoding_answer = recursive(encodings, step, numQ, numS)
    if encoding_answer.get_Encoding() is not "":
        display_results(numQ, encoding_answer)
    else:
        print("No solution found.")
    
    histogram(numS, steps)
    
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
def histogram(k, steps):
    bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    fig = plt.figure()
                              
    plt.hist(steps, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('Steps')
    plt.ylabel('Iterations')
    plt.title('Genetic Algorith for k=' + str(k))
    plt.legend()
    plt.show()
    fig.savefig('histogram.png')


def recursive(encodings, step, numQ, numS):
    
    encodings = gen_probabilities(encodings)
    goal = ncr(numQ, 2)
    
    encodings = gen_probabilities(encodings)
    for e in encodings:
        if e.get_Fitness() == goal:
            return e
        
    next_gen = selection(numQ, encodings)
    crossover_gen = crossover(next_gen, numS)
    mut_gen = mutation(crossover_gen) 
    step += 1
    print("Step ", step)
    return recursive(mut_gen, step, numQ, numS)

'''
    if encodings[0].get_Fitness() == goal:
        return encodings[0]
    else: 
        next_gen = selection(numQ, encodings)
        crossover_gen = crossover(next_gen, numS)
        mut_gen = mutation(crossover_gen)
        step += 1
        print("Step ", step)
        return recursive(mut_gen, step, numQ, numS)
            

    
    #for testing purposes
    
    print("probabilities for encodings:")
    for e in encodings:
        print(e.get_Probability())
        
    next_gen = selection(numQueens, encodings)
    print("encodings chosen for next generation")
    for e in next_gen:
        print(e.get_Probability())
    '''   
'''--------------------------------main_function is sort of same of solver function------------------------------''
def main_fuction(numQ, numS):
    numQ = int(numQ)
    numS = int(numS)
    goal = ncr(numQ, 2)
    step = 0
    encoding_answer = Encoding("") 
    population = gen_encodings(numQ, numS)
    
    print("current encodings")
    for item in population: 
        print (item.get_Encoding())
    
    i = 4
    not_found = True
    while (not_found):
        print("Step ", step)
        for item in population:
            #Check if individual item in the population meet the fitness goal
            if (item.get_Fitness() == goal):
                encoding_answer = item
                #not_found = False
                i = 0
                break
        
        #
        next_gen = selection(numQ, population)
        print("Seleted: ")
        for e in next_gen: 
            print (e.get_Encoding())
        #
        crossover_gen = crossover(next_gen, numS)
        print("Crossover: ")
        for e in crossover_gen: 
            print (e.get_Encoding())
        #
        mut_gen = mutation(crossover_gen) 
        print("Mutation")
        for e in mut_gen: 
            print (e.get_Encoding())
        
        step = step + 1
        print()
        population = mut_gen
        i = i - 1
    
    #encoding_answer = recursive(encodings, step, numQ, numS)    I don't think we need this here
    display_results(numQ, encoding_answer)
'''        
#main_function(4,2)
#nqueens_solver(5, 10)   
#----------MAIN----------
nqueens_solver(sys.argv[1], sys.argv[2])
