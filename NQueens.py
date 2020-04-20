# N Queens Problem
from constraint import Problem
from constraint import AllDifferentConstraint
from time import perf_counter
#from constraint import MinConflictSolver



# Solving using incremental approach
solver = [] # Stores time taken to solve each N
N = 1 # Variable
start,end=0,0
N = 1
while end-start<20: # The program would wait upto 5 minutes for solving a problem
    problem = Problem()
    cols = range(N)
    rows = range(N)
    problem.addVariables(cols, rows)
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(
                    lambda row1, row2, col1=col1,
                    col2=col2: abs(row1 - row2) !=
                    abs(col1 - col2) and row1 != row2,
                    (col1, col2),
                )
    
    start = perf_counter() # Starting Counter
    solutions = problem.getSolutions()
    end = perf_counter() # Ending Counter
    solver.append((N,end-start))

    print('Possible Solution for',N,'Queens Puzzle:', end=' ')
    if len(solutions)>0:
        solution = [(k, v) for k, v in solutions[-1].items()]
        for p in solution:
            print(p,end=' ')
        print()
    else:
        print('No solution')
    N+=1
# Solcing using iterative approach
