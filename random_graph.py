import networkx as nx
import random
import json

# cytoscape.js-compatible json from G
def cyto_json(G):
    my_json = nx.readwrite.json_graph.cytoscape_data(G)['elements']
    for node in my_json['nodes']:
        del node['data']['name'], node['data']['value']
        node['data']['label'] = node['data']['id']

    return json.dumps(my_json)


# connected graph with some randomness
def create_graph():
    G = nx.erdos_renyi_graph(random.randint(7,12), 0.4, directed=False)
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(random.randint(7,12), 0.4, directed=False)

    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = random.randint(17,42)
        
    return G

def get_json():
    return cyto_json(create_graph())
  
# if called from console  
if __name__ == "__main__":
    print(get_json())
