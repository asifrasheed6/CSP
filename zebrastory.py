from constraint import *

p = Problem()

#All variables (25 in total)
colors = ['Red', 'Green', 'White', 'Yellow', 'Blue']
nationalities = ['English', 'Spaniard', 'Japanese', 'Italian', 'Norwegian']
professions = ['Painter', 'Sculptor', 'Diplomat', 'Violinist', 'Doctor']
drinks = ['Tea', 'Coffee', 'Milk', 'Fruit Juice', 'Water']
pets = ['Dog', 'Snails', 'Fox', 'Horse', 'Zebra']

#All variables within their group will have range from 1 to 6 (indicates which Houses they belong to)
p.addVariables(colors, range(1, 6))
p.addVariables(nationalities, range(1, 6))
p.addVariables(professions, range(1, 6))
p.addVariables(drinks, range(1, 6))
p.addVariables(pets, range(1, 6))

#All variables within their group should be different
p.addConstraint(AllDifferentConstraint(), colors)
p.addConstraint(AllDifferentConstraint(), nationalities)
p.addConstraint(AllDifferentConstraint(), professions)
p.addConstraint(AllDifferentConstraint(), drinks)
p.addConstraint(AllDifferentConstraint(), pets)

#All constraints where variables belong to the same house
p.addConstraint(AllEqualConstraint(), ['English', 'Red'])
p.addConstraint(AllEqualConstraint(), ['Spaniard', 'Dog'])
p.addConstraint(AllEqualConstraint(), ['Japanese', 'Painter'])
p.addConstraint(AllEqualConstraint(), ['Italian', 'Tea'])
p.addConstraint(AllEqualConstraint(), ['Green', 'Coffee'])
p.addConstraint(AllEqualConstraint(), ['Sculptor', 'Snails'])
p.addConstraint(AllEqualConstraint(), ['Diplomat', 'Yellow'])
p.addConstraint(AllEqualConstraint(), ['Violinist', 'Fruit Juice'])

p.addConstraint(lambda n: n == 1, ['Norwegian']) #left most house is 1
p.addConstraint(lambda g, w: g == w + 1, ['Green', 'White']) #Green house to the right of White
p.addConstraint(lambda m: m == 3, ['Milk']) #milk in middle house
p.addConstraint(lambda n, b: n == b + 1 or n == b - 1, ['Norwegian', 'Blue']) #norwegian neighbour of blue house
p.addConstraint(lambda f, doc: f == doc + 1 or f == doc - 1, ['Fox', 'Doctor']) #fox neighbour of doctor
p.addConstraint(lambda h, dip: h == dip + 1 or h == dip - 1, ['Horse', 'Diplomat']) #horse neighbour of diplomat

sol = p.getSolutions()
print('Number of Solutions:', len(sol),'\n')

#storing all values of variables in their respective groups
color_vals = {sol[0][k] : k for k in colors}
nationalities_vals = {sol[0][k] : k for k in nationalities}
professions_vals = {sol[0][k] : k for k in professions}
drinks_vals = {sol[0][k] : k for k in drinks}
pets_vals = {sol[0][k] : k for k in pets}


for i in range(1, 6):
    print('Contents of House', i)
    print('-------------------')
    print('Color:', color_vals[i])
    print('Nationality:', nationalities_vals[i])
    print('Profession:', professions_vals[i])
    print('Drink:', drinks_vals[i])
    print('Pet:', pets_vals[i], '\n')





