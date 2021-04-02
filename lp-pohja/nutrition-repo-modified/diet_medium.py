import pandas as pd
from pulp import *


df = pd.read_excel("diet-medium.xlsx",nrows=17)


# df


# Create the 'prob' variable to contain the problem data
prob = LpProblem("Simple Diet Problem", LpMinimize)


# Creates a list of the Ingredients
food_items = list(df['Foods'])


print("So, the food items to consdier, are\n"+"-"*100)
for f in food_items:
    print(f,end=', ')


# ### Create a dictionary of costs for all food items

costs = dict(zip(food_items,df['Price/Serving']))


costs


# ### Create a dictionary of calories for all food items

calories = dict(zip(food_items,df['Calories']))


# ### Create a dictionary of cholesterol for all food items

cholesterol = dict(zip(food_items,df['Cholesterol (mg)']))


# ### Create a dictionary of total fat for all food items

fat = dict(zip(food_items,df['Total_Fat (g)']))


# ### Create a dictionary of sodium for all food items

sodium = dict(zip(food_items,df['Sodium (mg)']))


# ### Create a dictionary of carbohydrates for all food items

carbs = dict(zip(food_items,df['Carbohydrates (g)']))


# ### Create a dictionary of dietary fiber for all food items

fiber = dict(zip(food_items,df['Dietary_Fiber (g)']))


# ### Create a dictionary of protein for all food items

protein = dict(zip(food_items,df['Protein (g)']))


# ### Create a dictionary of vitamin A for all food items

vit_A = dict(zip(food_items,df['Vit_A (IU)']))


# ### Create a dictionary of vitamin C for all food items

vit_C = dict(zip(food_items,df['Vit_C (IU)']))


# ### Create a dictionary of calcium for all food items

calcium = dict(zip(food_items,df['Calcium (mg)']))


# ### Create a dictionary of iron for all food items

iron = dict(zip(food_items,df['Iron (mg)']))


# ### Create a dictionary of food items with lower bound

# A dictionary called 'food_vars' is created to contain the referenced Variables
food_vars = LpVariable.dicts("Food",food_items,0,cat='Continuous')


food_vars


# ### Adding the objective function to the problem

# The objective function is added to 'prob' first
prob += lpSum([costs[i]*food_vars[i] for i in food_items]), "Total Cost of the balanced diet"


# ### Adding the calorie constraints to the problem

prob += lpSum([calories[f] * food_vars[f] for f in food_items]) >= 800.0, "CalorieMinimum"
prob += lpSum([calories[f] * food_vars[f] for f in food_items]) <= 1300.0, "CalorieMaximum"


# ### Adding other nutrient constraints to the problem one by one...

# # Cholesterol
# prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) >= 30.0, "CholesterolMinimum"
# prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) <= 240.0, "CholesterolMaximum"
# 
# # Fat
# prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 40.0, "FatMinimum"
# prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= 100.0, "FatMaximum"
# 
# # Sodium
# prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) >= 500.0, "SodiumMinimum"
# prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) <= 2000.0, "SodiumMaximum"
# 
# # Carbs
# prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 130.0, "CarbsMinimum"
# prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= 450.0, "CarbsMaximum"
# 
# # Fiber
# prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) >= 125.0, "FiberMinimum"
# prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) <= 250.0, "FiberMaximum"
# 
# # Protein
# prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= 60.0, "ProteinMinimum"
# prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= 100.0, "ProteinMaximum"
# 
# # Vitamin A
# prob += lpSum([vit_A[f] * food_vars[f] for f in food_items]) >= 1000.0, "VitaminAMinimum"
# prob += lpSum([vit_A[f] * food_vars[f] for f in food_items]) <= 10000.0, "VitaminAMaximum"
# 
# # Vitamin C
# prob += lpSum([vit_C[f] * food_vars[f] for f in food_items]) >= 400.0, "VitaminCMinimum"
# prob += lpSum([vit_C[f] * food_vars[f] for f in food_items]) <= 5000.0, "VitaminCMaximum"
# 
# # Calcium
# prob += lpSum([calcium[f] * food_vars[f] for f in food_items]) >= 300.0, "CalciumMinimum"
# prob += lpSum([calcium[f] * food_vars[f] for f in food_items]) <= 1500.0, "CalciumMaximum"
# 
# # Iron
# prob += lpSum([iron[f] * food_vars[f] for f in food_items]) >= 10.0, "IronMinimum"
# prob += lpSum([iron[f] * food_vars[f] for f in food_items]) <= 40.0, "IronMaximum"

# Fat
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 20.0, "FatMinimum"
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= 50.0, "FatMaximum"

# Carbs
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 130.0, "CarbsMinimum"
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= 200.0, "CarbsMaximum"

# Fiber
prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) >= 60.0, "FiberMinimum"
prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) <= 125.0, "FiberMaximum"

# Protein
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= 100.0, "ProteinMinimum"
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= 150.0, "ProteinMaximum"


# ### Writing problem data to a `.lp` file

# The problem data is written to an .lp file
# prob.writeLP("SimpleDietProblem.lp")


# ### Run the solver

# The problem is solved using PuLP's choice of Solver
prob.solve()


# ### Print the problem solution status `'optimal'`, `'infeasible'`, `'unbounded'` etc...

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])


# ### Scan through the problem variables and print out only if the variable quanity is positive i.e. it is included in the optimal solution

print("Therefore, the optimal (least cost) balanced diet consists of\n"+"-"*110)
for v in prob.variables():
    if v.varValue>0:
        print(v.name, "=", v.varValue)


# ### Print the optimal diet cost

print("The total cost of this balanced diet is: ${}".format(round(value(prob.objective),2)))
