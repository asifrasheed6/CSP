from constraint import *
p = Problem()

#Variables have domains from 1 to 3 (inclusive)
#table 1 is closest to the door, then table 2, and farthest table 3
p.addVariable('IceSwan', range(1, 4))
p.addVariable('GoldLion', range(1, 4))
p.addVariable('MarblePyramid', range(1, 4))

#ice sculpture cant be on table next to door (i.e 1)
#animal sculptures can't be placed adjacent to each other (ice not next to gold)
def constr(ice, gold):
    return ice != 1 and ice != gold - 1 and ice != gold + 1

p.addConstraint(constr, ['IceSwan', 'GoldLion'])
#sculptures placed on different tables
p.addConstraint(AllDifferentConstraint(), ['IceSwan', 'GoldLion', 'MarblePyramid'])

for i in p.getSolutions():
    print('IceSwan placed on table:', i['IceSwan'],
          '\nGoldLion placed on table:', i['GoldLion'],
          '\nMarblePyramid placed on table:', i['MarblePyramid'])