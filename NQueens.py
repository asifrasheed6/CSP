# N Queens Problem
from constraint import Problem
from constraint import AllDifferentConstraint
from time import perf_counter
from constraint import MinConflictsSolver

# Solving using incremental approach
times = [] # Stores time taken to solve each N
N = 1 # Variable
start,end=0,0
N = 1 # Number of Queens
while end-start<20: # The program would wait upto 5 minutes for solving a problem
    problem = Problem()
    
    cols = range(N) # Number of Columns
    rows = range(N) # Number of Rows
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
    times.append((N,end-start)) # Stores Number of Queens and Time Taken to Solve the Puzzle
    N+=1

print('Total Time Taken to Solve The Puzzle using Incremental Approach:')
print('N\t Time')
for time in times:
    print(time[0],'\t',str(time[1])+' seconds')
    
# Solcing using iterative approach
print('\nIterative Approach')
times = [] # Stores time taken to solve each N
N = 1 # Variable
start,end=0,0
N = 1 # Number of Queens
while end-start<20: # The program would wait upto 5 minutes for solving a problem
    problem = Problem()
    
    cols = range(N) # Number of Columns
    rows = range(N) # Number of Rows
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
                
    problem.setSolver(MinConflictsSolver())
    start = perf_counter() # Starting Counter
    solution = problem.getSolution() # Minimum Conflict Solver only returns one solution
    end = perf_counter() # Ending Counter
    times.append((N,end-start)) # Stores Number of Queens and Time Taken to Solve the Puzzle
    N+=1

print('Total Time Taken to Solve The Puzzles using Iterative Approach:')
print('N\t Time')
for time in times:
    print(time[0],'\t',str(time[1])+' seconds')
