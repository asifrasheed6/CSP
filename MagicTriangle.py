# Magic Triangle Problem
from constraint import Problem
from constraint import ExactSumConstraint
from constraint import AllDifferentConstraint

# Magic triangle with 6 circles (3 on each side), so possible sum is 9,10,11 and 12
print('==========MAGIC TRIANGLE WITH 6 CIRCLES==========\n')
for S in range(9,13):
    problem = Problem()

    # Variables
    problem.addVariable('C1',range(1,7)) # Corner 1
    problem.addVariable('C2',range(1,7)) # Corner 2
    problem.addVariable('C3',range(1,7)) # Corner 3
    problem.addVariable('E1',range(1,7)) # Edge 1
    problem.addVariable('E2',range(1,7)) # Edge 2
    problem.addVariable('E3',range(1,7)) # Edge 3

    # Constraints
    problem.addConstraint(ExactSumConstraint(S,[1,1,1]),['C1','E1','C3']) # Side 1
    problem.addConstraint(ExactSumConstraint(S,[1,1,1]),['C2','E2','C1']) # Side 2
    problem.addConstraint(ExactSumConstraint(S,[1,1,1]),['C3','E3','C2']) # Side 3
    problem.addConstraint(AllDifferentConstraint(),['C1','C2','C3','E1','E2','E3']) # Values in each circle are unique
    
    solutions = problem.getSolutions()
    print('Total Number of Possible Solutions for Sum',S,':',len(solutions))
    # Prints only one solution
    print('  ',solutions[-1]['C1'],'')
    print('',solutions[-1]['E1'],' ',solutions[-1]['E2'])
    print(solutions[-1]['C3'],'',solutions[-1]['E3'],'',solutions[-1]['C2'])
    print()
    
# Magic triangle with 9 circles (4 on each side), so possible sum is 17,19,20,21,23
print('==========MAGIC TRIANGLE WITH 9 CIRCLES==========\n')
for S in range(17,24):
    problem = Problem()

    # Variables
    problem.addVariable('C1',range(1,10)) # Corner 1
    problem.addVariable('C2',range(1,10)) # Corner 2
    problem.addVariable('C3',range(1,10)) # Corner 3
    problem.addVariable('E11',range(1,10)) # Side 1, Edge 1
    problem.addVariable('E12',range(1,10)) # Side 1, Edge 2
    problem.addVariable('E21',range(1,10)) # Side 2, Edge 1
    problem.addVariable('E22',range(1,10)) # Side 2, Edge 2
    problem.addVariable('E31',range(1,10)) # Side 3, Edge 1
    problem.addVariable('E32',range(1,10)) # Side 3, Edge 2

    # Constraints
    problem.addConstraint(ExactSumConstraint(S,[1,1,1,1]),['C1','E11','E12','C3']) # Side 1
    problem.addConstraint(ExactSumConstraint(S,[1,1,1,1]),['C2','E21','E22','C1']) # Side 2
    problem.addConstraint(ExactSumConstraint(S,[1,1,1,1]),['C3','E31','E32','C2']) # Side 3
    problem.addConstraint(AllDifferentConstraint(),['C1','C2','C3','E11','E12','E21','E22','E31','E32']) # Values in each circle are unique
        
    solutions = problem.getSolutions()
    print('Total Number of Possible Solutions for Sum',S,':',len(solutions))
    # Prints only one solution
    if len(solutions)>0:
        print('  ',solutions[-1]['C1'])
        print(' ',solutions[-1]['E21'],'',solutions[-1]['E11'])
        print('',solutions[-1]['E22'],'  ',solutions[-1]['E12'])
        print(solutions[-1]['C2'],solutions[-1]['E31'],solutions[-1]['E32'],'',solutions[-1]['C3'])
    print()
