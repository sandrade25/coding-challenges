import pytest
import sys


sys.path.append("../../")
import random


from worksheets.b_traversal.breadth_first_traversal import breadth_first_traversal
from worksheets.b_traversal.depth_first_traversal import depth_first_traversal

from protected.worksheets_answers.b_traversal.breadth_first_traversal import breadth_first_traversal as breadth_first_traversal_a
from protected.worksheets_answers.b_traversal.depth_first_traversal import depth_first_traversal as depth_first_traversal_a


class TestTraversal:
    def test_depth_first_traversal(self, graph, binary_tree):
        answer1 = []
        depth_first_traversal_a(graph, 'a', answer1)
        answer2 = []
        depth_first_traversal_a(binary_tree, 'a', answer2)

        user1 = depth_first_traversal(graph, 'a')
        assert user1 is not None, "solution not yet provided"

        user2 = []
        depth_first_traversal(binary_tree, 'a', user2)

        assert user1 == answer1
        assert user2 == answer2

    def test_breadth_first_traversal(self, graph, binary_tree):
        answer1 = breadth_first_traversal_a(graph, 'a')
        answer2 = breadth_first_traversal_a(binary_tree, 'a')

        user1 = breadth_first_traversal(graph, 'a')
        assert user1 is not None, "solution not yet provided"

        user2 = breadth_first_traversal(binary_tree, 'a')

        assert user1 == answer1
        assert user2 == answer2

    



