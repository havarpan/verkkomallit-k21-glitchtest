import pulp

def my_lp_problem():

    # Niemi, esim. 3.2.1
  
    # LpMinimize vai LpMaximize (nimeä emme käytä)
    my_lp = pulp.LpProblem('nimi', pulp.LpMaximize)
 
    # muuttujien määrittely
    x1 = pulp.LpVariable('x1', lowBound=0, upBound=9, cat='Continuous')
    x2 = pulp.LpVariable('x2', lowBound=0, upBound=5, cat='Continuous')

    # mitä halutaan minimoida / maksimoida
    my_lp += x1 + 3*x2

    # ja millä ehdoilla
    my_lp += 5*x1 + 6*x2 <= 60
    my_lp += -1*x1 + x2 <= 3
    
    return my_lp