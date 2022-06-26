from collections import deque


"""
given a graph. 
print out the correct order of nodes based on breadth first search.
"""

def breadth_first_traversal(graph, root):
    q = deque([root])
    v = []
    while q:
        n = q.popleft()
        v.append(n)
        for node in graph[n]:
            if node not in v and node not in q:
                q.append(node)
    return v