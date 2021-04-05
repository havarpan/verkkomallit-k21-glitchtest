import pulp
import json
import sys

sys.path.append('python/ryhma1')
from ryhma1 import my_lp_problem

# tekninen apufunktio
def solve_lp(lp):

    var, prob = pulp.LpProblem.from_dict(lp.to_dict())
  
    prob.solve()
    
    mydict = {'objective': prob.objective.value()}
    for x in var:
        mydict[x] = var[x].value()
        
    return json.dumps(mydict)
  

# ryhmä 1
def ryhma1():
    return solve_lp(my_lp_problem())

# ryhmä 2
def ryhma2():
    return solve_lp(my_lp_problem())
