from constraint import *
p = Problem()
p.addVariables(['Poland', 'Germany', 'Czech Republic', 'Slovakia', 'Hungary', 'Austria', 'Switzerland', 'Slovenia', 'Italy'],
               ['red', 'green', 'blue', 'yellow'])

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

p.addConstraint(constraints, ['Poland', 'Germany', 'Czech Republic', 'Slovakia', 'Hungary', 'Austria', 'Switzerland', 'Slovenia', 'Italy'])
for x,y in p.getSolution().items():
    print(x + ':', y)


