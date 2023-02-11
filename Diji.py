import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
c= int(input("enter edge number"))
source_ver = [1,1,2,2,2,3,4]
dest_ver = [2,4,3,4,5,5,5]
wts = [6,1,5,2,2,5,1]
weigh=[]
for i in range(0,c):
#   a=str(input("enter source vertex"))
#   b=str(input("enter destination vertex"))
#   d=int(input("enter weight"))
  a = source_ver[i]
  b = dest_ver[i]
  d = wts[i]
  G.add_edge(a,b,weight=d)
  source_ver.append(a)
  dest_ver.append(b)
  wts.append(d)
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
print("original graph")
nx.draw_networkx_edge_labels(G,pos,edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()})
plt.show()

source_node = int (input("Enter source node :"))
target_node = int (input("Enter target node :"))
shortest_path=nx.dijkstra_path(G, source_node, target_node)

pos2=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
print("shortest_path from ", source_node, " to ", target_node)
nx.draw_networkx_edge_labels(G,pos,edge_labels={(u,v): G[u][v]['weight'] for u,v in G.edges()})
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)], edge_color='r', width=2)
plt.show()
f=0
j=0
for i in range(len(source_ver)):
    if j<len(shortest_path)-1:
        if source_ver[i]==shortest_path[j] and dest_ver[i]==shortest_path[j+1]:
            weigh.append(wts[i])
            print(source_ver[i],"-",dest_ver[i],":",wts[i])
            j+=1

print("the length of shortest path is ",sum(weigh))
