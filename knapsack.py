################################################################################
# Author:   Evan Dietrich
# Course:   Comp 131 - Intro AI
# Prof:     Santini
#
# Assign:   Genetic Algorithms
# Date:     11/10/2020
# File:     knapsack.py
################################################################################

################################################################################
#       IMPORTS + GLOBALS
################################################################################

import sys
import os
import math
import random
import numpy as np
import time

# Given + Mutation likelihood
MAX_WEIGHT = 250
CULL_POP = 0.50
MUT_LIKE = 0.05

# User can alter other parameters to run different simulations
NUM_RUNS = 6
MAX_ITER = 600
MAX_TIME = 0.60

################################################################################
#       Box Class: Constructs Boxes from Complete Set of the Problem Statement
################################################################################

class Box:
    # Initial vals
    def __init__(self, number, weighting, importance):
        self.number = number
        self.weighting = weighting
        self.importance = importance

    # Helper for printing the optimized potential knapsack/box combos
    def __str__(self):
        return "Box #" + str(self.number) + \
           " weighs " + str(self.weighting) + \
           " and has importance " + str(self.importance) + "."

################################################################################
#       Genetic Algorithm Class: Implements Algo for culling/determining fitness
################################################################################

class GeneticAlgo:
    total_weighting, total_importance = 0, 0

    # Initial vals
    def __init__(self, cull_pop):
        self.cull_pop = cull_pop
        for box in BOXES:
            self.total_weighting += box.weighting
            self.total_importance += box.importance

    # Creates a random population from randomly generated individuals
    def createRandomPop(self):
        count, pop = 15, []
        for x in range(count):
            indiv = []
            for y in range(len(BOXES)):
                indiv.append(random.choice([True, False]))
            pop.append(indiv)
        return pop
    
    # Gives overall importance/weighting of boxes in curr selection attempt
    # (baesd on fitness function); then update score by accounting for penalty
    def fitness(self, selection):
        weighting, importance, score = 0, 0, 0
        for box in selection:
            weighting += box.weighting
            importance += box.importance

        score = importance - (self.total_weighting * (max(0, weighting - MAX_WEIGHT)/600)) 
        return importance, weighting, score

    # Sorts population by fitness function method & gets highest score overall,
    # by first finding fitness score of each individual in current population
    def fitnessSort(self, pop):
        sorted_list = []
        for x, indiv in enumerate(pop):
            importance, weighting, score = self.fitness(BOXES[indiv])
            sorted_list.append((indiv, importance, weighting, score))

        # Reorganize by seperately-indexed arrangement
        sorted_list.sort(key=lambda temp: temp[3], reverse=True)
        return [var[0] for var in sorted_list], sorted_list[0][3]

    # Recombination/Crossover Mutation by randomly selecting point to swap
    # genetic material around, applied on both indivduals
    def crossoverMutation(self, x, y):
        cross_pt = random.randint(1, len(x))
        return (x[:cross_pt] + y[cross_pt:]), (y[:cross_pt] + x[cross_pt:])

    # Fringe Mutation by randomly/slightly changing phenotype of given indivdual
    # Essentially swapping the truth value at index in list/array
    def fringeMutation(self, x):
        rand_pt = random.randint(0, len(x)-1)
        x[rand_pt] = not x[rand_pt]
        return x

    #  The "main()" of our GA, initializes again for each run per NUM_RUNS
    def run(self, pop):
        start_time = time.time()
        num_iters, top_score, best_run, best_run_iteration = 0, 0, 0, 0

        # Start by sorting population by fitness as defined by fitness function
        while True:
            pop, curr_score = self.fitnessSort(pop)

            # Simple Greedy Algo to retain best overall run
            if (best_run == 0) or (curr_score > top_score):
                best_run = pop[0]
                best_run_iteration = num_iters
                top_score = curr_score
            
            # Takes ordered-by-fitness population & keeps top 50% of individuals
            culled_half = int(len(pop) * (1 - self.cull_pop))
            update_pop = pop[:culled_half]

            # Calls mutation functions applied to randomly chosen 2 individuals
            size = len(update_pop)
            for x in range(size):
                indiv_1, indiv_2 = random.sample(update_pop, 2)
                cross_1, cross_2 = self.crossoverMutation(indiv_1, indiv_2)

                if (np.random.uniform(0, 1) < MUT_LIKE):
                    cross_1 = self.fringeMutation(cross_1)
                update_pop.append(cross_1)
            
            # Update population & increment overall model
            pop = update_pop
            num_iters += 1
                
            # Check for early break if over max iterations / max time limits
            if (num_iters >= MAX_ITER) or (time.time() >= start_time +MAX_TIME):
                break

        return best_run

################################################################################
#       MAIN PROGRAM
################################################################################

# List of Boxes (Number / Weighting / Importance) from Problem Statement.
BOXES = np.array([
    Box(1, 20, 6), Box(2, 30, 5), Box(3, 60, 8), Box(4, 90, 7), Box(5, 50, 6),
    Box(6, 70, 9), Box(7, 30, 4), Box(8, 30, 5), Box(9, 70, 4), Box(10, 20, 9),
    Box(11, 20, 2), Box(12, 60, 1)])

def organizeKnapsack():
    # Runs algo # of times per user's decree
    for x in range(NUM_RUNS):
        ga = GeneticAlgo(CULL_POP)
        pop = ga.createRandomPop()
        combo = ga.run(pop)

        # Present possible Knapsack/Box combo
        print("**********************************************")
        print("Run #" + str(x+1) + " at max iterations [" + str(MAX_ITER) + "]")
        print("& max seconds of [" + str(MAX_TIME) + "]")
        print("**********************************************")

        print(">>> A possible Knapsack contains the following boxes:\n")
        for box in BOXES[combo]:
            print(box)
        weighting, importance, final_score = ga.fitness(BOXES[combo])
        print(">>> Final Run Score is: " + str(final_score) + "\n")

# Runtime header then begins organization routine (determines optimal solutions)
if __name__ == '__main__':
    print("\n>>> Running Genetic Algorithm on: " + str(len(BOXES)) + " BOXES")
    print(">>> Knapsack Max Weight: " + str(MAX_WEIGHT) + "\n")
    organizeKnapsack()
