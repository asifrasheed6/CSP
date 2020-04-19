from constraint import *
p = Problem()
europe = ['Poland', 'Germany', 'Czech Republic', 'Slovakia', 'Hungary', 'Austria', 'Switzerland', 'Slovenia', 'Italy']
colors = ['red', 'green', 'blue', 'yellow']

p.addVariables(europe, colors)

def constraints(pol, ger, cze, slovak, hun, aus, switz, sloven, it):
    if pol in [ger, cze, slovak]:
        return False
    elif ger in [cze, aus, switz]:
        return False
    elif cze in [slovak, aus]:
        return False
    elif slovak in [hun, aus]:
        return False
    elif aus in [hun, sloven, switz, it]:
        return False
    elif sloven in [it, hun]:
        return False
    elif switz in [it]:
        return False
    return True

p.addConstraint(constraints, europe)
sol = p.getSolutions()
print('Number of solutions (with min. 4 colors):', len(sol), '\n')
print('Solution:\n')
for x,y in sol[0].items():
    print(x + ':', y)


