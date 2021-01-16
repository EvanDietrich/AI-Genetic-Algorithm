**********************************
Author:   Evan Dietrich
Course:   Comp 131 - Intro AI
Prof:     Santini

Assign:   Genetic Algorithms
Date:     11/10/2020
File:     README.md
**********************************

Overview:
This program implements a solution to the backpack problem by making it as
valuable as possible without exceeding the max weight, using a genetic
algorithm-based approach. 

Technical Breakdown:
knapsack.py   - Runs the program.  
README.md     - Instructions to run program and assignment overview.

Running the Program:
To run the program, ensure all downloaded files are on your machine, and run
"python3 knapsack.py" on your terminal screen. This will start the program
for a automated running procedure. The procedure given is controlled by the
global variables (essentially, parameter options for runtime) found in the 
'IMPORTS + GLOBALS' section of the 'knapsack.py' file. The example run is with:

MAX_WEIGHT = 250
CULL_POP = 0.50
MUT_LIKE = 0.05

NUM_RUNS = 6
MAX_ITER = 600
MAX_TIME = 0.60

By editing the globals, you can test the knapsack organizer in different
scenarios, and observe the execution of the algorithm strategy. Currently, per
decree of the Problem Statement, we have MAX_WEIGHT set to 250 and CULL_POP set
to 50%, as we are ensuring we do not exceed the maximum knapsack weight and we
are culling the population by 50% at every generation. The mutation likelihood
applies here only to the fringe mutation, as the crossover mutation will occur
at each iteration. I chose to implement this solution with a number of globals
as it provides many parameters to optimize with, as you can imagine using grid
search methodology on these 6 main parameters to increase your understanding
of what may provide an optimal solution.

When you run the program, you will noticed 6 different "simulations", providing
a hypothetical knapsack/box combo that you could pack with. On each of my tests,
summed weights would come to 250, or very rarely 240 depending on lowering some
parameter values (especially MAX_ITERS and MAX_TIME) which I discovered during
testing. I provide a hypothetical score based on the "importance" of the boxes,
which is also factored into the main GA algo. I believe I have completed this
assignment in full (defining the problem as a GA, providing the genome, defining
fringe ops, & culling the lower half of the population at each generation).

Collaborators:
I completed this assignment with assistance from the student posts and
instructor answers on the Comp131 Piazza page, with the lecture material,
our class textbook, and an online article on the use of GA's in ML:
"https://www.softwaretestinghelp.com/genetic-algorithms-in-ml/", which provided
some more intuition into the problem via ML applications, as well as described
additional selection methods for creating mutations, beyond the couple examples
we covered in lecture.

Notes:
Testing my solution by increasing the number of seconds did not seem to increase
the performance of my generated knapsack/box combos greatly, while reducing the
time and number of iterations did seem to lower the refinement of my program.
