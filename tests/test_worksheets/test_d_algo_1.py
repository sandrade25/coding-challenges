import pytest
import sys


sys.path.append("../../")
import random
from protected.worksheets_answers.d_algo_1.dijkstras_shortest_path import dijkstras_shortest_path as dijkstras_shortest_path_a
from worksheets.d_algo_1.dijkstras_shortest_path import dijkstras_shortest_path


from worksheets.d_algo_1.dfs_connected_cell_in_grid import dfs_connected_cell_in_grid
from protected.worksheets_answers.d_algo_1.dfs_connected_cell_in_grid import dfs_connected_cell_in_grid as dfs_connected_cell_in_grid_a

from worksheets.d_algo_1.breadth_first_island_count import breadth_first_island_count
from protected.worksheets_answers.d_algo_1.breadth_first_island_count import breadth_first_island_count as breadth_first_island_count_a

from worksheets.d_algo_1.longest_common_substring import longest_common_substring
from protected.worksheets_answers.d_algo_1.longest_common_substring import longest_common_substring as longest_common_substring_a




class TestAlgo1:

    def test_longest_common_subtring(self, list_of_words):
        words = [
            random.choices(list_of_words, k=2),
            random.choices(list_of_words, k=2),
            random.choices(list_of_words, k=2)
        ]
        for word_group in words:
            user = longest_common_substring(word_group[0], word_group[1])
            answer = longest_common_substring_a(word_group[0], word_group[1])
            assert user is not None, "solution not yet provided"

            assert answer is not None
            assert user == answer

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

    def test_dfs_connected_cell_in_grid(self, binary_grid1, binary_grid2, binary_grid3, binary_grid4):
        answer1 = dfs_connected_cell_in_grid_a(binary_grid1)
        assert answer1 == 8
        answer2 = dfs_connected_cell_in_grid_a(binary_grid2)
        assert answer2 == 5
        answer3 = dfs_connected_cell_in_grid_a(binary_grid3)
        assert answer3 == 10
        answer4 = dfs_connected_cell_in_grid_a(binary_grid4)
        assert answer4 == 1

        user1 = dfs_connected_cell_in_grid(binary_grid1)
        assert user1 is not None, "solution not yet provided"
        user2 = dfs_connected_cell_in_grid(binary_grid2)
        user3 = dfs_connected_cell_in_grid(binary_grid3)
        user4 = dfs_connected_cell_in_grid(binary_grid4)

        assert answer1 == user1
        assert answer2 == user2
        assert answer3 == user3
        assert answer4 == user4

    def test_breadth_first_island_count(self, binary_grid1, binary_grid2, binary_grid3, binary_grid4, binary_grid5):
        answer1 = breadth_first_island_count_a(binary_grid1)
        assert answer1 == 1
        answer2 = breadth_first_island_count_a(binary_grid2)
        assert answer2 == 2
        answer3 = breadth_first_island_count_a(binary_grid3)
        assert answer3 == 2
        answer4 = breadth_first_island_count_a(binary_grid4)
        assert answer4 == 13
        answer5 = breadth_first_island_count_a(binary_grid5)
        assert answer5 == 5

        user1 = breadth_first_island_count(binary_grid1)
        assert user1 is not None, "solution not yet provided"
        user2 = breadth_first_island_count(binary_grid2)
        user3 = breadth_first_island_count(binary_grid3)
        user4 = breadth_first_island_count(binary_grid4)
        user5 = breadth_first_island_count(binary_grid5)

        assert answer1 == user1
        assert answer2 == user2
        assert answer3 == user3
        assert answer4 == user4
        assert answer5 == user5
    



