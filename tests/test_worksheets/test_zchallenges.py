import pytest
import sys
sys.path.append("../../")
import random
# from worksheets.zchallenges.array_manipulation import 
# from worksheets.zchallenges.bfs_shortest_reach_in_graph import 
# from worksheets.zchallenges.breadth_first_island_count import 
# from worksheets.zchallenges.depth_first_cycle import 

# from worksheets.zchallenges.matrix import 
# from worksheets.zchallenges.minimum_swaps_2 import 
# from worksheets.zchallenges.roads_and_libraries import 
from worksheets.zchallenges.two_d_array import two_d_array
from worksheets_answers.zchallenges.two_d_array import two_d_array as two_d_array_a
from worksheets.zchallenges.dfs_connected_cell_in_grid import dfs_connected_cell_in_grid
from worksheets_answers.zchallenges.dfs_connected_cell_in_grid import dfs_connected_cell_in_grid as dfs_connected_cell_in_grid_a





class TestZChallenges:
    def test_two_d_array(self, word_board):
        board, words_in_board = word_board
        words_list_false = ['float', 'buy', 'trumpet', 'parked', 'interrupt']
        
        answer1 = two_d_array_a(board, words_in_board)
        answer2 = two_d_array_a(board, words_list_false)

        user1 = two_d_array(board, words_in_board)
        assert user1 is not None, "solution not yet provided"
        user2 = two_d_array(board, words_list_false)

        assert answer1 == user1
        assert answer2 == user2

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


        


    


        





