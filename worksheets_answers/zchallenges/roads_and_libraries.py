#https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs


"""

given the input:
n = count of cities
c_lib = cost of each library
c_road = cost of each road to connect two cities
cities = array of possible connections between cities represented as edges ([parent, child])

calculate the minimum cost to ensure every city has access to a library.
a city has access if it can travel any number of roads to get to a city with a library built within. 

in some cases it may be cheaper to build libraries in each city.

"""
from collections import deque

def bfs(graph):
    visited = {node:False for node in graph}
    
    roads = 0
    libraries = 0
        
    nodes_left = [node for node in graph]
    while nodes_left:
        new_node = nodes_left.pop()
        if visited[new_node]:
            continue
        
        queue = deque([(new_node, None)])
        visited[new_node] = True
        
        while queue:
            node, parent = queue.popleft()
            
            if not parent:
                libraries += 1
                
            for n in graph[node]:
                if not visited[n]:
                    queue.append((n, node))
                    roads += 1
                    visited[n] = True
                    
    return roads, libraries
    

def make_graph(n, arr):
    graph = {i:[] for i in range(n)}
    for parent, child in arr:
        graph[parent].append(child)
        graph[child].append(parent)
    return graph 


def roads_and_libraries(cities, n, c_lib, c_road, ):
    graph = make_graph(n, cities)
        
    roads, libraries = bfs(graph)
    cost_several_libraries = c_lib * len(graph)
    cost_roads_and_libraries = (roads * c_road) + (c_lib * libraries)
    return min(cost_roads_and_libraries, cost_several_libraries)