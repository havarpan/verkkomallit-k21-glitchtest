import pulp

my_lp = pulp.LpProblem('testi', pulp.LpMaximize)
 
x1 = pulp.LpVariable('x1', lowBound=0, upBound=700, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, upBound=450, cat='Continuous')

# objective function
my_lp += 60*x1 + 100*x2

# constraints
my_lp += x1 + x2 <= 600
my_lp += 2*x1 + 3*x2 <= 1600

# solve
my_lp.solve()
