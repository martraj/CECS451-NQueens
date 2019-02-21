# CECS451-NQueens
CECS 451 - Artificial Intelligence: n-queens solver using a genetic algorithm

Selection

- Our selection algorithm uses Stochastic Uniform Sampling (SUS) to select 75\% of the current population to create the next generation. This approach offers the most ``fair'' selection process in comparison to the following methods: Roulette Wheel Selection, Ranked Selection, and Tournament Selection. The aforementioned methods tend to favor the most fit parent and choose them more frequently over the others. SUS strives to  choose the fittest parents while simultaneously eliminating the less fit parents, more inline to actual genetic selection of dominate traits over recessive ones. It should be noted our current SUS implementation does not work for negative fitness values. 

Crossover

- Crossover algorithm is one of the main types of genetic algorithm. It is the recombination of the genetic information of two parents to generate new offsprings. Specifically, in our crossover operation, we use one-point crossover. One random point position of the parents’ gene is selected to crossover. The tails of two parents gene will swap with each other and produce two offspring gene. The gene of the first offspring is the combination of the first parent gene up to the crosspoint and the rest of its gene is from the second parent. Similarly, the second offspring gene is the combination of the second parent gene up to the crosspoint and the rest of its gene is from the first parent.


Mutation

- For our mutation algorithm, we used the Random Resetting Mutation Operator.  This operator is an extension of Bit Flip Mutation.  In this operation, a randomly selected gene is changed to a random value.  In our case, we first select a random index of the string that holds the queens position.  Then, a random value is generated in the range [0, length of string), which represents a valid row position on the board.  The previous value at the selected index is then set to this new random value.

