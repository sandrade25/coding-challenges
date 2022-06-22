
from collections import deque

"""
using dijkstras shortest path,
find fasted path from starting node to end.
"""

def dijkstras_shortest_path(graph, start, end):
    # setup base table.
    # need to track the shortest path to a node from start, and what the previous vertex that led here is.

    # initialize list of UNVISITED NODES

    # do below process until unvisted list is empty

    # find node with shortest distance currently that is still unvisited.
    # initial run should produce starting node.

    # do things with min node.
    # if the minnode distance + the weight of any of its neighboring nodes is less than the existing weight
    # of its neirhboring nodes, then update the shortest distance to neighboring node, and its previous vertex
    # that got it to this new shortest distance.

    # now that table is fully populated with shortest distance to each node (from the start),
    # and also with the previous node that gets to each nodes shortest_dist,
    # we can trace backwards through the table starting from the endpoint until we hit the start point.

    shortest_dist = {k: 9999999 for k in graph}
    parents = {k: '' for k in graph}
    unvisited = [k for k in graph]
    parents[start] = None
    shortest_dist[start] = 0

    while unvisited:
        min_node = None
        for i in range(len(unvisited)):
            if min_node is None:
                min_node = i
            elif shortest_dist[unvisited[i]] < shortest_dist[unvisited[min_node]]:
                min_node = i
        min_node = unvisited.pop(min_node)

        neighbors = graph[min_node]
        for node, weight in neighbors.items():
            if weight + shortest_dist[min_node] < shortest_dist[node]:
                shortest_dist[node] = weight + shortest_dist[min_node]
                parents[node] = min_node

    node = end
    path = deque([])
    while node:
        path.appendleft(node)
        node = parents[node]
    return path