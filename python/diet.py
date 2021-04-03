import pandas as pd
import pulp as lp

# Read 64 rows of diet.xlsx into a pandas DataFrame object
df = pd.read_excel("diet.xlsx", nrows=64)

# Creates a list of the Ingredients
food_items = list(df['Foods'])

print("Food items to consider:\n"+"-"*80)
for f in food_items:
    print(f, end=', ')

# Create a dictinary of costs for all food items
costs = dict(zip(food_items,df['Price/ Serving']))

print('Costs:', costs)

# Create dictionaries for nutrition items
calories = dict(zip(food_items,df['Calories']))
cholesterol = dict(zip(food_items,df['Cholesterol mg']))
fat = dict(zip(food_items,df['Total_Fat g']))
sodium = dict(zip(food_items,df['Sodium mg']))
carbs = dict(zip(food_items,df['Carbohydrates g']))
fiber = dict(zip(food_items,df['Dietary_Fiber g']))
protein = dict(zip(food_items,df['Protein g']))
vit_A = dict(zip(food_items,df['Vit_A IU']))
vit_C = dict(zip(food_items,df['Vit_C IU']))
calcium  = dict(zip(food_items,df['Calcium mg']))
iron = dict(zip(food_items,df['Iron mg']))

# Create a dictionary of food items with lower bound
food_vars = lp.LpVariable.dicts("Food", food_items, 0, cat='Continuous')

print('Food variables:', food_vars)

# Create the 'prob' variable to contain the problem data
prob = lp.LpProblem("Diet Problem", lp.LpMinimize)


# Add the objective function
prob += lp.lpSum([costs[i]*food_vars[i] for i in food_items]), "Total Cost of the balanced diet"


# Add constraints one by one

# Calories
prob += lp.lpSum([calories[f] * food_vars[f] for f in food_items]) >= 1500.0, "CalorieMinimum"
prob += lp.lpSum([calories[f] * food_vars[f] for f in food_items]) <= 2500.0, "CalorieMaximum"

# Cholesterol
prob += lp.lpSum([cholesterol[f] * food_vars[f] for f in food_items]) >= 30.0, "CholesterolMinimum"
prob +=lp.lpSum([cholesterol[f] * food_vars[f] for f in food_items]) <= 240.0, "CholesterolMaximum"

# Fat
prob +=lp.lpSum([fat[f] * food_vars[f] for f in food_items]) >= 20.0, "FatMinimum"
prob +=lp.lpSum([fat[f] * food_vars[f] for f in food_items]) <= 70.0, "FatMaximum"

# Sodium
prob +=lp.lpSum([sodium[f] * food_vars[f] for f in food_items]) >= 800.0, "SodiumMinimum"
prob +=lp.lpSum([sodium[f] * food_vars[f] for f in food_items]) <= 2000.0, "SodiumMaximum"

# Carbs
prob +=lp.lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 130.0, "CarbsMinimum"
prob +=lp.lpSum([carbs[f] * food_vars[f] for f in food_items]) <= 450.0, "CarbsMaximum"

# Fiber
prob +=lp.lpSum([fiber[f] * food_vars[f] for f in food_items]) >= 125.0, "FiberMinimum"
prob +=lp.lpSum([fiber[f] * food_vars[f] for f in food_items]) <= 250.0, "FiberMaximum"

# Protein
prob +=lp.lpSum([protein[f] * food_vars[f] for f in food_items]) >= 60.0, "ProteinMinimum"
prob +=lp.lpSum([protein[f] * food_vars[f] for f in food_items]) <= 100.0, "ProteinMaximum"

# Vitamin A
prob +=lp.lpSum([vit_A[f] * food_vars[f] for f in food_items]) >= 1000.0, "VitaminAMinimum"
prob +=lp.lpSum([vit_A[f] * food_vars[f] for f in food_items]) <= 10000.0, "VitaminAMaximum"

# Vitamin C
prob +=lp.lpSum([vit_C[f] * food_vars[f] for f in food_items]) >= 400.0, "VitaminCMinimum"
prob +=lp.lpSum([vit_C[f] * food_vars[f] for f in food_items]) <= 5000.0, "VitaminCMaximum"

# Calcium
prob +=lp.lpSum([calcium[f] * food_vars[f] for f in food_items]) >= 700.0, "CalciumMinimum"
prob +=lp.lpSum([calcium[f] * food_vars[f] for f in food_items]) <= 1500.0, "CalciumMaximum"

# Iron
prob +=lp.lpSum([iron[f] * food_vars[f] for f in food_items]) >= 10.0, "IronMinimum"
prob +=lp.lpSum([iron[f] * food_vars[f] for f in food_items]) <= 40.0, "IronMaximum"


# The problem is solved using PuLP's choice of Solver
prob.solve()


print("Status:", lp.LpStatus[prob.status])

 
print("Optimal (least cost) balanced diet:\n"+"-"*110)
for v in prob.variables():
    if v.varValue>0:
        print(v.name, "=", v.varValue)


print("Optimal cost: ${}".format(round(lp.value(prob.objective),2)))
