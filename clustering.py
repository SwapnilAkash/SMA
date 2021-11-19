from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from numpy import random
import time
import networkx as nx
import networkx.algorithms.community as nx_comm

graph1 = nx.read_gml('karate.gml', label = 'id')
graph2 = nx.read_gml('dolphins.gml')
graph3 = nx.read_weighted_edgelist('jazz.net')

# graph1

matt = nx.to_numpy_matrix(graph1)

old_time = time.time()

spectral_clustering = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities in the graph
spectral_clustering.fit(matt)

new_time = time.time()
print("Time taken : ", new_time - old_time)

# find the nodes forming the communities
dataframe = spectral_clustering.labels_

ls = [[] for i in range(4)]

i = 1
for val in dataframe:
    if(val == 0):
        ls[0].append(i)
        i += 1
    elif(val == 1):
        ls[1].append(i)
        i += 1
    elif(val == 2):
        ls[2].append(i)
        i += 1
    elif(val == 3):
        ls[3].append(i)
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters : {}".format(len(ls)))
print("Modularity : " + str(nx_comm.modularity(graph1, ls)))
print("\n")


# graph2

matt = nx.to_numpy_matrix(graph2)

# convert graph to a list
lsg2 = list(graph2)

old_time = time.time()

spectral_clustering = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities in the graph
spectral_clustering.fit(matt)

new_time = time.time()
print("Time taken : ", new_time - old_time)

# find the nodes forming the communities
dataframe = spectral_clustering.labels_

ls = [[] for i in range(4)]

i = 0
for val in dataframe:
    if(val == 0):
        ls[0].append(lsg2[i])
        i += 1
    elif(val == 1):
        ls[1].append(lsg2[i])
        i += 1
    elif(val == 2):
        ls[2].append(lsg2[i])
        i += 1
    elif(val == 3):
        ls[3].append(lsg2[i])
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters : {}".format(len(ls)))
print("Modularity : " + str(nx_comm.modularity(graph2, ls)))
print("\n")


# G3

matt = nx.to_numpy_matrix(graph3)

old_time = time.time()

spectral_clustering = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# find communities in the graph
spectral_clustering.fit(matt)

new_time = time.time()
print("Time taken : ", new_time - old_time)

# find the nodes forming the communities
dataframe = spectral_clustering.labels_

ls = [[] for i in range(4)]

i = 1
for val in dataframe:
    if(val == 0):
        ls[0].append(str(i))
        i += 1
    elif(val == 1):
        ls[1].append(str(i))
        i += 1
    elif(val == 2):
        ls[2].append(str(i))
        i += 1
    elif(val == 3):
        ls[3].append(str(i))
        i += 1
        

print("Clusters : ")
print(ls)
print("Number of Clusters : {}".format(len(ls)))
print("Modularity : " + str(nx_comm.modularity(graph3, ls)))
print("\n")
