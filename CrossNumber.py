# Cross Number Grid Generator
from constraint import Problem
from constraint import MinConflictsSolver

problem = Problem()

'''
    The Grid:
        1. There are 10 constraints in total.
        2. All the numbers should be a multiple of 9.
        2. Solution 1 has 5 digits and meet Solution 3 at its 4rd digit and Solution 5a at its 2nd digit
        3. Solution 2 has 4 digits and meet Solution 3 at its 2nd digit and Solution Solution 5a at its 1st digit
        4. Solution 3 has 5 digits and meet Solution 2 at its 1st digit and Solution 1 at its 4th digit
        5. Solution 4 has 5 digits and meet Solution 8 at its 4th digit
        6. Solution 5 needs 2 solution, 5a is across with 3 digits and meets Solution 2 at its 2nd digit and Solution 1 at its 1st digit, 5b is down with 6 digits and meet Solution 8 at its 2nd digit and Solution 9 at its 4th digit
        7. Solution 6 has 2 digits and meet with Solution 9 at its 1st digit
        8. Solution 7 has 4 digits and meet with Solution 9 at its 1st digit
        9. Solution 8 has 3 digits and meet with Solution 4 at its 2nd digit and Solution 5b at its 3rd digit
        10.Solution 9 has 7 digits and meets with Solution 5b at its 5th digit, Solution 6 at its 1st digit, Solution 10 at its 3rd digit and Solution 7 at its 4th digit
        11.Solution 10 has 2 digits and meets with Solution 9 at its 1st digit
'''

# Variables
problem.addVariable('1',range(10**4,10**5)) # Solution 1 has 5 digits
problem.addVariable('2',range(10**3,10**4)) # Solution 2 has 4 digits
problem.addVariable('3',range(10**4,10**5)) # Solution 3 has 5 digits
problem.addVariable('4',range(10**4,10**5)) # Solution 4 has 5 digits
problem.addVariable('5a',range(10**2,10**3)) # Solution 5a has 3 digits
problem.addVariable('5b',range(10**5,10**6)) # Solution 5b has 6 digits
problem.addVariable('6',range(10**1,10**2)) # Solution 6 has 2 digits
problem.addVariable('7',range(10**3,10**4)) # Solution 7 has 4 digits
problem.addVariable('8',range(10**2,10**3)) # Solution 8 has 3 digits
problem.addVariable('9',range(10**6,10**7)) # Solution 9 has 7 digits
problem.addVariable('10',range(10**1,10**2)) # Solution 10 has 2 digits

# Constraints
problem.addConstraint(lambda a,b,c: str(a)[3]==str(b)[3] and str(a)[1]==str(c)[0], ['1','3','5a'] )
problem.addConstraint(lambda a,b,c: str(a)[1]==str(b)[1] and str(a)[0]==str(c)[1], ['2','3','5a'] )
problem.addConstraint(lambda a,b: str(a)[3]==str(b)[1], ['4','8'])
problem.addConstraint(lambda a,b,c: str(a)[1]==str(b)[2] and str(a)[3]==str(c)[4], ['5b','8','9'])
problem.addConstraint(lambda a,b: str(a)[0]==str(b)[0], ['6','9'])
problem.addConstraint(lambda a,b: str(a)[0]==str(b)[3], ['7','9'])
problem.addConstraint(lambda a,b: str(a)[2]==str(b)[0], ['9','10'])

problem.setSolver(MinConflictsSolver())
solution = problem.getSolution()

print('Number 1(Down):',solution['1'])
print('Number 2(Down):',solution['2'])
print('Number 3(Across):',solution['3'])
print('Number 4(Down):',solution['4'])
print('Number 5(Across):',solution['5a'])
print('Number 5(Down):',solution['5b'])
print('Number 6(Down):',solution['6'])
print('Number 7(Down):',solution['7'])
print('Number 8(Across):',solution['8'])
print('Number 9(Across):',solution['9'])
print('Number 10(Down):',solution['10'])
