import pulp

def my_lp_problem():
  
    # LpMinimize vai LpMaximize (nimeä emme käytä)
    my_lp = pulp.LpProblem('nimi', pulp.LpMaximize)
 
    # muuttujien määrittely
    x = pulp.LpVariable('x', lowBound=0, upBound=700, cat='Continuous')
    y = pulp.LpVariable('y', lowBound=0, upBound=450, cat='Continuous')

    # mitä halutaan minimoida / maksimoida
    my_lp += 60*x + 100*y

    # ja millä ehdoilla
    my_lp += x + y <= 600
    my_lp += 2*x + 3*y <= 1600
    
    return my_lp