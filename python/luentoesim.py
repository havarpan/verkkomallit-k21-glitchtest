import networkx as nx
# import pulp

G = nx.DiGraph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

G.add_edges_from([('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'F'), ('D', 'C'), ('E', 'C'), ('E', 'D'), ('E', 'F')])
capacities = [4,5,5,4,4,3,2,2,1]
costs = [1,7,7,2,3,2,1,1,4]

for i, edge in enumerate(G.edges()):
    G.edges[edge]['capacity'] = capacities[i]
    G.edges[edge]['cost'] = costs[i]

demands = [-2,-5,-1,3,2,3]

for i, node in enumerate(G.nodes()):
    G.nodes[node]['demand'] = demands[i]

myflow = nx.min_cost_flow(G, weight='cost')
mycost = nx.cost_of_flow(G, myflow, weight='cost')
print(mycost, myflow)
