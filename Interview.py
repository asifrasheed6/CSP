# Interview Scheduling Problem
from constraint import Problem
from constraint import AllDifferentConstraint

problem = Problem()

# The poosible appointment times are 1, 2, 3 or 4
# There are four applicants: Ali, Bob, Cyl, and Dan

problem.addVariable('Ali',[1,3,4])# Ali is busy from 2 to 3
problem.addVariable('Dan',[1,4]) # Dan is busy from 2 to 4
# Bob and Cyl are free before 4
problem.addVariable('Bob',[1,2,3])
problem.addVariable('Cyl',[1,2,3])

# All the time allocated should be different
problem.addConstraint(AllDifferentConstraint(),['Ali','Dan','Bob','Cyl'])

# Possible Schedules without considering preferences
solutions = problem.getSolutions()

print('Possible Schedules (without considering preferences): ')
for solution in solutions:
    print('Ali:',str(solution['Ali'])+'pm,','Dan:',str(solution['Dan'])+'pm,','Bob:',str(solution['Bob'])+'pm,','Cyl:',str(solution['Cyl'])+'pm')

# Giving the earliest appoinment to Cyl
problem.addConstraint(lambda ali,dan,bob,cyl: cyl==min(ali,dan,bob,cyl), ['Ali','Dan','Bob','Cyl'])

# Possible Schedules considering preferences
solutions = problem.getSolutions()

print('Possible Schedules (considering preferences): ')
for solution in solutions:
    print('Ali:',str(solution['Ali'])+'pm,','Dan:',str(solution['Dan'])+'pm,','Bob:',str(solution['Bob'])+'pm,','Cyl:',str(solution['Cyl'])+'pm')
