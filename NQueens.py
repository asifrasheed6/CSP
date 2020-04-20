# N Queens Problem
from constraint import Problem
from constraint import AllDifferentConstraint
from constraint import MinConflictSolver

problem = Problem()

# Solcing using incremental approach
# Variable
N = int(input('Enter N:'))
for i in range(N):
    problem.addVariable(i,[(i,j) for i in range(N) for j in range(N)]) # All the possible location in the chess board is added as tuples

# Constraints
problem.addConstraint(AllDifferentConstraint(), [i for i in range(N)]) # The Queens should be placed in diifferent sqares

def cells(*args): # No two Queens are in the same row or column and diagonally aligned
    for i in range(len(args)):
        for j in range(1,len(args)):
            if (args[i][0]==args[j][0] or args[i][1]==args[j][1] or abs(args[i][0]-args[j][0])==abs(args[i][1]-args[j][1])) and i!=j:
                return False
    return True
problem.addConstraint(cells, [i for i in range(N)])

solutions = problem.getSolutions()
print('Possible Solutions for the Puzzle:')
if len(solutions)>0:
    for i in range(N):
        print(solutions[-1][i],end=' ')
    print()

# Solcing using iterative approach
