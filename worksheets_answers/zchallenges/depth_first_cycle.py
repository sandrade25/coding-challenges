"""
https://www.techiedelight.com/check-undirected-graph-contains-cycle-not/

Check if an undirected graph contains a cycle or not

Given a connected undirected graph, check if it contains any cycle or not.
Can you both breadth first and depth first search for this. 
Try it using depth first search here.

input will look like and array consisting of tuples (parent, child)

eg:
[
        (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
        (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
        # edge (10, 11) introduces a cycle in the graph
    ]

can setup graph however is easiest. but above is the input.
"""

def make_graph(arr):
    g = {}
    for src, dst in arr:
        if not g.get(src):
            g[src] = set()

        if not g.get(dst):
            g[dst] = set()
        
        g[src].add(dst)
        g[dst].add(src)
        
    return g

def dfs(graph, node, visited=[], parent=-1):

    visited.append(node)
    for next_node in graph[node]:
        if next_node not in visited:
            if dfs(graph, next_node, visited, node):
                return True
        elif next_node != parent:
            return True
    return False


def depth_first_cycle(graph_arr):
    graph = make_graph(graph_arr)
    return dfs(graph, graph_arr[0][0], [])

