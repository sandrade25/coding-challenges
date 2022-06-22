import pytest
import sys
sys.path.append("../../")
import random
# from worksheets.zchallenges.array_manipulation import 
# from worksheets.zchallenges.bfs_shortest_reach_in_graph import 
# from worksheets.zchallenges.breadth_first_island_count import 
# from worksheets.zchallenges.depth_first_cycle import 
# from worksheets.zchallenges.dfs_connected_cell_in_grid import 
# from worksheets.zchallenges.matrix import 
# from worksheets.zchallenges.minimum_swaps_2 import 
# from worksheets.zchallenges.roads_and_libraries import 
from worksheets.zchallenges.two_d_array import two_d_array
from worksheets_answers.zchallenges.two_d_array import two_d_array as two_d_array_a





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


    


        





