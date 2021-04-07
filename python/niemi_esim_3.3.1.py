import pulp

my_lp = pulp.LpProblem('testi', pulp.LpMaximize)
 
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Continuous')
x5 = pulp.LpVariable('x5', lowBound=0, cat='Continuous')

# objective function
my_lp += 0.1264*x1 + 0.107*x2 + 0.0764*x3 + 0.064*x4 + 0.0769*x5

# constraints
my_lp += x1 + x2 + x3 + x4 + x5 == 500000
my_lp += x1 + x2 <= 250000
my_lp += x4 + x5 >= 150000
my_lp += 2*x1 + 8*x2 - 2*x3 - 5*x4 + x5 <= 0

# solve
my_lp.solve()

# tämä on yksi tapa saada muuttujatkin näkyviin
# ehkä pieni mutka siinä, muttei se paljon haittaa
var, prob = pulp.LpProblem.from_dict(my_lp.to_dict())
mydict = {'objective': prob.objective.value()}
for x in var:
    mydict[x] = var[x].value()
print(mydict)
