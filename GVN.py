import numpy as np
import networkx as nx
from tabulate import tabulate
import matplotlib.pyplot as plt
import networkx.algorithms.community as nx_comm
import time


def edge_to_remove(graph):
    G_dict = nx.edge_betweenness_centrality(graph)
    edge = ()

  # extract the edge with highest edge betweenness centrality score
    for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
        edge = key
        break
        
    return edge


def girvan_newman(graph):
    # find number of connected components
    sg = nx.connected_components(graph)
    sg_count = nx.number_connected_components(graph)

    while(sg_count == 1):
        graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
        sg = nx.connected_components(graph)
        sg_count = nx.number_connected_components(graph)

    return sg

graph1 = nx.read_gml('karate.gml', label = 'id')
graph2 = nx.read_gml('dolphins.gml')
graph3 = nx.read_weighted_edgelist('jazz.net')

print("Karate Dataset: ")
print("Number of nodes: {}".format(nx.number_of_nodes(graph1)))
print("Number of edges: {}".format(nx.number_of_edges(graph1)))
print("Average Path Length: {}".format(nx.average_shortest_path_length(graph1)))
print("Average Clustering Coefficient: {}".format(nx.average_clustering(graph1)))
print("\n")

print("Dolphins Dataset: ")
print("Number of nodes: {}".format(nx.number_of_nodes(graph2)))
print("Number of edges: {}".format(nx.number_of_edges(graph2)))
print("Average Path Length: {}".format(nx.average_shortest_path_length(graph2)))
print("Average Clustering Coefficient: {}".format(nx.average_clustering(graph2)))
print("\n")

print("Jazz Dataset: ")
print("Number of nodes: {}".format(nx.number_of_nodes(graph3)))
print("Number of edges: {}".format(nx.number_of_edges(graph3)))
print("Average Path Length: {}".format(nx.average_shortest_path_length(graph3)))
print("Average Clustering Coefficient: {}".format(nx.average_clustering(graph3)))
print("\n")

# graph1
start_time = time.time()

# find communities in the graph
c1 = girvan_newman(graph1.copy())

# find the nodes forming the communities
node_groups1 = []

for i in c1:
    node_groups1.append(list(i))

current_time = time.time()
time_taken = current_time - start_time

print("Clusters from Karate Dataset : ")
print(node_groups1)   
print("Number of Clusters: {}".format(len(node_groups1)))   
print("Modularity : " + str(nx_comm.modularity(graph1, node_groups1)))
print("Time Taken : {}".format(time_taken))
print("\n")

# graph2
start_time = time.time()

# find communities in the graph
c2 = girvan_newman(graph2.copy())

# find the nodes forming the communities
node_groups2 = []

for i in c2:
    node_groups2.append(list(i))

current_time = time.time()
time_taken = current_time - start_time

print("Clusters from Dolphins Dataset : ")
print(node_groups2)    
print("Number of Clusters: {} ".format(len(node_groups2)))  
print("Modularity : " + str(nx_comm.modularity(graph2, node_groups2)))
print("Time Taken : {}".format(time_taken))
print("\n")

# graph3
start_time = time.time()

# find communities in the graph
c3 = girvan_newman(graph3.copy())

# find the nodes forming the communities
node_groups3 = []

for i in c3:
    node_groups3.append(list(i))

current_time = time.time()
time_taken = current_time - start_time

print("Clusters from Jazz Dataset : ")
print(node_groups3)  
print("Number of Clusters : {}".format(len(node_groups3)))
print("Modularity : " + str(nx_comm.modularity(graph3, node_groups3)))
print("Time Taken : {}".format(time_taken))