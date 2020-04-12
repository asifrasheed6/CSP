## Constraint Programming
From https://stackabuse.com/constraint-programming-with-python-constraint/:
1. Install python module **python-constraint** : `pip3 install python-constraint`
  - The way we need to think is different for constraint programming because the usual way of programming 
that we are familiar with is imperative programming while constraint programming requires declarative 
programming.

  - Imperative Programming: the developer describes the solution/algorithm for achieving the goal by 
changing the program state through assignment statements and executing instructions step by step. So
the order of the instructions is important.

  - Declarative Programming: We describe the goal instead of the steps to achieve the goal like we do in
something like SQL.

2. To use the module: `import constraint`
3. Describe a variable as our problem 
4. Add variables and their respective domains(intervals) to our problem (Set X and Set D)
5. Add constraints to our problem (Set C)
6. Fetch the solutions
7. Look at the solutions to find the one that we are looking for 

Look at the example code below to make some sense:
```
from constraint import Problem

problem = Problem() # From Step 3 above

problem.addVariable('x',[1,2,3]) # From Step 4 above, look at the syntax:
# problem_variable.addVariable(variable,domain)
# Variable here: x, Domain: {1,2,3}
problem.addVariable('y',range(10)) # From Step 4 above, look at the syntax again:
# problem_variable.addVariable(variable,domain)
# Variable here: y, Domain: 0 <= y <10

# For Step 5, we need to define a function that checks whether constraints are met for the given values
# Our constraint here is x + y >= 5
def constraint(x,y):
    if x+y==10:
        return True
    return False

problem.addConstraint(constraint,['x','y'])
# Here 'x' and 'y' are keys to retrive x and y respeectively
# Makee sure that the key you give here and in Step 4 are the same
# The order in which the keys are given doesn't matter
solutions = problem.getSolutions() # solutions is a set of dictionary
# Each dictionary contain the possible pair of x and y

print('All possible solutions for X and Y: ')
for solution in solutions:
    print('x:', solution['x'], 'y:', solution['y'])
    
# Alternatively, ignore from line 14
from constraint import ExactSumConstraint

problem2 = Problem()
problem2.addVariable('x',[1,2,3])
problem2.addVariable('y',range(10))

problem2.addConstraint(ExactSumConstraint(10,[1,1]),'xy') # 'xy' and ['x','y'] are the same
# The above code means 1*x + 1*y = 10
# We could use ExactSumConstraint instead of the function
# The syntax is ExactSumConstraint(sum,[number of times var 1 is multiplied, ...]
# Example for 2*x + 2*y == 10:
#                               ExactSumConstraint(10,[2,2])

solutions = problem2.getSolutions()
print('All possible solutions for X and Y: ')
for solution in solutions:
    print('x:', solution['x'], 'y:', solution['y'])

# Similarly we have AllDifferentConstraint where all the values would be unique

# Reading a JSON file
import json
import constraint

data = {'name':'Test File', 'description': 'We will store this data in file'}
# This is where we are going to store the data

# To write to the json file
with open('test.json', 'w') as openfile:
    json.dump(data,openfile) # will write the dictionary to the file

print()
# To read from the json file
with open('test.json') as openfile:
    var = json.load(openfile) # would load the file as dictionary
    print(var['name'])
    print(var['description'])

# Sudoku Solver using JSON file:
print('\n====SUDOKU SOLVER====')

sudoku = Problem()

# Adding variables 11 to 99 with domains 1 to 9 each
# Also 11 means (1,1), 12 means (1,2)....99 means (9,9)
for i in range(1,10):
    sudoku.addVariables(range(i*10+1,i*10+10), range(1,10))

# Constraint: all values in a row must be unique
for i in range(1,10):
    sudoku.addConstraint(constraint.AllDifferentConstraint(), range(i*10+1,i*10+10))

# Constraint: all values in a column must be unique
for i in range(1,10):
    sudoku.addConstraint(constraint.AllDifferentConstraint(), range(10+i,100+i,10))

# Constraint: all the nine 3x3 squares should have unique values
for i in [1,4,7]:
    for j in [1,4,7]:
        square = [10*i+j,10*i+j+1,10*i+j+2,10*(i+1)+j,10*(i+1)+j+1,10*(i+1)+j+2,10*(i+2)+j,10*(i+2)+j+1,10*(i+2)+j+2]
        sudoku.addConstraint(constraint.AllDifferentConstraint(), square)

board = None
with open('sudoku.json') as openfile:
    board = json.load(openfile)

# Adding constraint to each cell in the Matrix if it is empty
for i in range(9):
    for j in range(9):
        if board[i][j] != 0: # 0 means the cell is empty
            def c(variable_value, value_in_table = board[i][j]):
                if variable_value == value_in_table:
                    return True
            sudoku.addConstraint(c, [((i+1)*10 + (j+1))])
            # So basically we are making sure that the program won't modify
            # the value already on the sodoku board

solution = sudoku.getSolutions()

# Printing all the possible solutions:
for s in solution:
    print("=====================")
    for i in range(1,10):
        print('|',end=' ')
        for j in range(1,10):
            print(s[i*10+j],end=' ')
            if(j==9):
                print('|\n')
    print("=====================")

```


