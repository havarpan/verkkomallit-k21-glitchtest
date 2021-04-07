import pulp
import json
import sys

# ryhmä 1
sys.path.append('python/ryhma1')
from ryhma1 import ryhma1_lp_problem

# ryhmä 2
sys.path.append('python/ryhma2')
from ryhma2 import ryhma2_lp_problem

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
    return solve_lp(ryhma1_lp_problem())

# ryhmä 2
def ryhma2():
    return solve_lp(ryhma2_lp_problem())
