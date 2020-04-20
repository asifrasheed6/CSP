# N Queens Problem
from constraint import Problem
from constraint import AllDifferentConstraint

problem = Problem()

# Variable
N = int(input('Enter the number of Queens: '))
for i in range(N):
    problem.addVariable(i,[(i,j) for i in range(8) for j in range(8)]) # All the possible location in the chess board is added as tuples

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
for solution in solutions:
    for i in range(N):
        print(solution[i],end=' ')
    print()
