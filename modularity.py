from networkx.algorithms.community.modularity_max import greedy_modularity_communities
import time
import networkx as nx
import networkx.algorithms.community as nx_comm

graph1 = nx.read_gml('karate.gml', label = 'id')
graph2 = nx.read_gml('dolphins.gml')
graph3 = nx.read_weighted_edgelist('jazz.net')

# graph1
start_time = time.time()

# find communities in the graph
c1 = greedy_modularity_communities(graph1)

current_time = time.time()
print("Time taken : ", current_time - start_time)

# find the nodes forming the communities
node_groups1 = (list(sorted(c) for c in c1))

print("Clusters : ")
print(node_groups1)   
print("Number of Clusters : {}".format(len(node_groups1)))
print("Modularity : " + str(nx_comm.modularity(graph1, node_groups1)))
print("\n")

# graph2
start_time = time.time()

# find communities in the graph
c2 = greedy_modularity_communities(graph2)

current_time = time.time()
print("Time taken : ", current_time - start_time)

# find the nodes forming the communities
node_groups2 = (list(sorted(c) for c in c2))

print("Clusters : ")
print(node_groups2)   
print("Number of Clusters : {}".format(len(node_groups2)))
print("Modularity : " + str(nx_comm.modularity(graph2, node_groups2)))
print("\n")


# graph3
start_time = time.time()

# find communities in the graph
c3 = greedy_modularity_communities(graph3)

current_time = time.time()
print("Time taken : ", current_time - start_time)

# find the nodes forming the communities
node_groups3 = (list(sorted(c) for c in c3))

print("Clusters : ")
print(node_groups3)   
print("Number of Clusters : {}".format(len(node_groups3)))
print("Modularity : " + str(nx_comm.modularity(graph3, node_groups3)))