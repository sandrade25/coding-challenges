


"""
given a graph. 
print out the correct order of nodes based on depth first search.
"""

def depth_first_traversal(graph, node, v=[]):
    v.append(node)
    for n in graph[node]:
        if n not in v:
            depth_first_traversal(graph, n, v)
    return v

