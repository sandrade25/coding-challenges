#https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

"""
given an array of edges (parent, child) and n=count of nodes, 
find the shortest distance to each node from a starting node. 
assume a distance of 6 for each edge

If a node cannot be reached from the starting node, 
return -1 for that node. 

output should be an array of distances from starting node to node

EG:
input:
    edges = [(1,2), (2,3), (3,4), (1,5)]
    n = 6
    start = 1

output = [6, 12, 18, 6, -1]
^
6 -> node 1 to 2
12 -> node 1 to 3
18 -> node 1 to 4
6 -> node 1 to 5 (directly connected)
-1 -> node 1 to 6 (6 does not share an edge with 1)


some similarities here with dijkstras shortest path
"""

def bfs_shortest_reach_in_graph(edges, node_count, start):
    return 






    


    
