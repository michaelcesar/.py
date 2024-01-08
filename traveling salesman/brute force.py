import json
import time
import networkx as nx
import itertools
import matplotlib.pyplot as plt

def calc_cost(way, costs):
    cost = 0
    for i in range(len(way)):
        current_node = way[i]
                        #ciclo hamiltoniano
        next_node = way[(i + 1) % len(way)]
                #somando custo usando o dicionário
        cost += costs.get(current_node, {}).get(next_node, float('inf'))
    return cost


def brute_force(costs):

    #obtendo nós
    nodes = list(costs.keys())
    
    best_way, min_cost = None, float('inf')

    for way in itertools.permutations(nodes):
        current_cost = calc_cost(way, costs)
        if current_cost < min_cost:
            min_cost = current_cost
            best_way = way

    return best_way, min_cost

def interface(costs, best_way):
    
    G = nx.Graph()

 
    best_route_edges = [(best_way[i], best_way[i+1]) for i in range(len(best_way) - 1)]

    for node, connections in costs.items():
        for destiny, distance in connections.items():
            
            if (node, destiny) in best_route_edges or (destiny, node) in best_route_edges:
                color = 'green'
            else:
                color = 'black'
            G.add_edge(node, destiny, weight=distance, color=color)
    return G

def main():
   
    with open(f'grafo.json', 'r') as json_file:
        costs = json.load(json_file)

    start = time.perf_counter()

    best_way, total_cost = brute_force(costs)

    #list
    best_way = list(best_way)

    #fechando o ciclo hamiltoniano
    best_way.append(best_way[0])
    grafo = interface(costs, best_way)
    pos = nx.spring_layout(grafo)
    labels = nx.get_edge_attributes(grafo, 'weight')
    colors = nx.get_edge_attributes(grafo, 'color').values()
    nx.draw(grafo, pos, with_labels=True, edge_color=colors)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show(block=False)

    end = time.perf_counter()
    duration = end - start

    print(f"Melhor Rota: {best_way}\nDuração: {duration:.2f} segundos")
    print(f"Custo Total da Melhor Rota: {total_cost:.2f}")
    plt.pause(60)

if __name__ == "__main__":
    main()
