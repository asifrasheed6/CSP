from constraint import *

#SEND + MORE = MONEY (without carry)
p = Problem()

p.addVariables('SM', range(1, 10)) #leading characters can't be 0
p.addVariables('ENDORY', range(10))

def constraint(s, m, e, n, d, o, r, y):
    return (s*1000 + e*100 + n*10 + d) + (m*1000 + o*100 + r*10 + e) == (m*10000 + o*1000 + n*100 + e*10 + y)

p.addConstraint(constraint, 'SMENDORY')
p.addConstraint(AllDifferentConstraint(), 'SMENDORY') #all should have different digits

print('SEND + MORE = MONEY (without carry)\n-----------------------------------')
for i in p.getSolutions():
    print('{}{}{}{} + {}{}{}{} = {}{}{}{}{}'.format(i['S'], i['E'], i['N'], i['D'], i['M'], i['O'], i['R'], i['E'],
                                                    i['M'], i['O'], i['N'], i['E'], i['Y']))



#SEND + MORE = MONEY (with explicit carry)
p2 = Problem()

#IJK are the explictly defined carries (can have only 0 or 1 as domain)
p2.addVariables('IJK', range(2))
p2.addVariables('SM', range(1, 10))
p2.addVariables('ENDORY', range(10))

def constraint2(s, m, e, n, d, o, r, y, i, j, k):
    return (s + m + i == o + 10*m) and (e + o + j == n + i*10) and (n + r + k == e + j*10 ) and (d + e == y + k*10)

p2.addConstraint(constraint2, 'SMENDORYIJK')
p2.addConstraint(AllDifferentConstraint(), 'SMENDORY') #All have to be different

print('\nSEND + MORE = MONEY (with explicit carries)\n-------------------------------------------')
for i in p2.getSolutions():
    print('{}{}{}{} + {}{}{}{} = {}{}{}{}{}'.format(i['S'], i['E'], i['N'], i['D'], i['M'], i['O'], i['R'], i['E'],
                                                    i['M'], i['O'], i['N'], i['E'], i['Y']))



#DEC - BIN = OCT (base 8)
p3 = Problem()

p3.addVariables('DBO', range(1, 8))
p3.addVariables('EICNT', range(8))

def constraint3(d, b, o, e, i, c, n, t):
    return (d*8*8 + e*8 + c) - (b*8*8 + i*8 + n) == (o*8*8 + c*8 + t)

p3.addConstraint(constraint3, 'DBOEICNT')
p3.addConstraint(AllDifferentConstraint(), 'DBOEICNT')

SUB = str.maketrans('8', '₈')

print('\n(DEC)8 - (BIN)8 = (OCT)8\n------------------------'.translate(SUB))
for i in p3.getSolutions():
    print('({}{}{})8 - ({}{}{})8 = ({}{}{})8'.translate(SUB).format(i['D'], i['E'], i['C'], i['B'], i['I'], i['N'], i['O'], i['C'], i['T']))




#EXTRA + DAY = LEAP + YEAR
p4 = Problem()

p4.addVariables('EDLY', range(1, 10))
p4.addVariables('XTRAP', range(10))

def constraint4(e, d, l, y, x, t, r, a, p):
    return (e*10000 + x*1000 + t*100 + r*10 + a) + (d*100 + a*10 + y) == (l*1000 + e*100 + a*10 + p) + (y*1000 + e*100 + a*10 + r)

p4.addConstraint(constraint4, 'EDLYXTRAP')
p4.addConstraint(AllDifferentConstraint(), 'EDLYXTRAP')

print('\nEXTRA + DAY = LEAP + YEAR\n-------------------------')
for i in p4.getSolutions():
    print('{}{}{}{}{} + {}{}{} = {}{}{}{} + {}{}{}{}'.format(i['E'], i['X'], i['T'], i['R'], i['A'], i['D'], i['A'], i['Y'],
                                                             i['L'], i['E'], i['A'], i['P'], i['Y'], i['E'], i['A'], i['R']))
