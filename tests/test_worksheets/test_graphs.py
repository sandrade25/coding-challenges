import pytest
import sys
sys.path.append("../../")
import random
from protected.worksheets_answers.graphs.dijkstras_shortest_path import dijkstras_shortest_path as dijkstras_shortest_path_a
from worksheets.graphs.dijkstras_shortest_path import dijkstras_shortest_path

class TestGraphs:
    def test_dijkstras_shortest_path(self, weighted_graph):
        
        answer1 = dijkstras_shortest_path_a(weighted_graph, "s", "t")
        answer2 = dijkstras_shortest_path_a(weighted_graph, "t", "b")
        answer3 = dijkstras_shortest_path_a(weighted_graph, "d", "s")

        user1 = dijkstras_shortest_path(weighted_graph, "s", "t")
        assert user1 is not None, "solution not yet provided"
        user2 = dijkstras_shortest_path(weighted_graph, "t", "b")
        user3 = dijkstras_shortest_path(weighted_graph, "d", "s")
        
        assert user1 == answer1
        assert user2 == answer2
        assert user3 == answer3
    





