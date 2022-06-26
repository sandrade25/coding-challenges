import pytest
import sys
sys.path.append("../../")
import random
# from worksheets.zchallenges.array_manipulation import 

# from worksheets.zchallenges.matrix import 
# from worksheets.zchallenges.minimum_swaps_2 import 
from worksheets.zchallenges.roads_and_libraries import roads_and_libraries
from worksheets_answers.zchallenges.roads_and_libraries import roads_and_libraries as roads_and_libraries_a
from worksheets.zchallenges.dfs_word_in_board import dfs_word_in_board
from worksheets_answers.zchallenges.dfs_word_in_board import dfs_word_in_board as dfs_word_in_board_a
from worksheets.zchallenges.dfs_connected_cell_in_grid import dfs_connected_cell_in_grid
from worksheets_answers.zchallenges.dfs_connected_cell_in_grid import dfs_connected_cell_in_grid as dfs_connected_cell_in_grid_a
from worksheets.zchallenges.depth_first_cycle import depth_first_cycle
from worksheets_answers.zchallenges.depth_first_cycle import depth_first_cycle as depth_first_cycle_a
from worksheets.zchallenges.breadth_first_island_count import breadth_first_island_count
from worksheets_answers.zchallenges.breadth_first_island_count import breadth_first_island_count as breadth_first_island_count_a
from worksheets.zchallenges.bfs_shortest_reach_in_graph import  bfs_shortest_reach_in_graph
from worksheets_answers.zchallenges.bfs_shortest_reach_in_graph import  bfs_shortest_reach_in_graph as bfs_shortest_reach_in_graph_a







class TestZChallenges:
    def test_dfs_word_in_board(self, word_board):
        board, words_in_board = word_board
        words_list_false = ['float', 'buy', 'trumpet', 'parked', 'interrupt']
        
        answer1 = dfs_word_in_board_a(board, words_in_board)
        answer2 = dfs_word_in_board_a(board, words_list_false)

        user1 = dfs_word_in_board(board, words_in_board)
        assert user1 is not None, "solution not yet provided"
        user2 = dfs_word_in_board(board, words_list_false)

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

    def test_depth_first_cycle(self, graph_arr_with_cycle, graph_arr_no_cycle):
        answer1 = depth_first_cycle_a(graph_arr_with_cycle)
        assert answer1 == True
        answer2 = depth_first_cycle_a(graph_arr_no_cycle)
        assert answer2 == False

        user1 = depth_first_cycle(graph_arr_with_cycle)
        assert user1 is not None, "solution not yet provided"
        user2 = depth_first_cycle(graph_arr_no_cycle)


        assert answer1 == user1
        assert answer2 == user2

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

    def test_bfs_shortest_reach_in_graph(self, graph_arr_with_cycle, graph_arr_no_cycle):

        answer1 = bfs_shortest_reach_in_graph_a(graph_arr_with_cycle, 13, 0)
        assert answer1 == [6, 12, 18, 18, 12, 6, 6, 12, 18, 18, 12, -1]
        answer2 = bfs_shortest_reach_in_graph_a(graph_arr_no_cycle, 13, 0)
        assert answer2 == [6, 12, 18, 18, 12, 6, 6, 12, 18, 18, 12, -1]
        answer3 = bfs_shortest_reach_in_graph_a(graph_arr_with_cycle, 12, 0)
        assert answer3 == [6, 12, 18, 18, 12, 6, 6, 12, 18, 18, 12]
        answer4 = bfs_shortest_reach_in_graph_a(graph_arr_no_cycle, 12, 0)
        assert answer4 == [6, 12, 18, 18, 12, 6, 6, 12, 18, 18, 12]

        user1 = bfs_shortest_reach_in_graph(graph_arr_with_cycle, 13, 0)
        assert user1 is not None, "solution not yet provided"
        user2 = bfs_shortest_reach_in_graph(graph_arr_no_cycle, 13, 0)
        user3 = bfs_shortest_reach_in_graph(graph_arr_with_cycle, 12, 0)
        user4 = bfs_shortest_reach_in_graph(graph_arr_no_cycle, 12, 0)


        assert answer1 == user1
        assert answer2 == user2
        assert answer3 == user3
        assert answer4 == user4

    def test_roads_and_libraries(self, graph_arr_with_cycle, graph_arr_no_cycle):

        answer1 = roads_and_libraries_a(graph_arr_with_cycle, 13, 5, 1 )
        assert answer1 == 31
        answer2 = roads_and_libraries_a(graph_arr_no_cycle, 13, 6, 2)
        assert answer2 == 46
        answer3 = roads_and_libraries_a(graph_arr_with_cycle, 12, 5, 1)
        assert answer3 == 26
        answer4 = roads_and_libraries_a(graph_arr_no_cycle, 12, 7, 8)
        assert answer4 == 84

        user1 = roads_and_libraries(graph_arr_with_cycle, 13, 5, 1)
        assert user1 is not None, "solution not yet provided"
        user2 = roads_and_libraries(graph_arr_no_cycle, 13, 6, 2)
        user3 = roads_and_libraries(graph_arr_with_cycle, 12, 5, 1)
        user4 = roads_and_libraries(graph_arr_no_cycle, 12, 7, 8)


        assert answer1 == user1
        assert answer2 == user2
        assert answer3 == user3
        assert answer4 == user4
  




        


    


        





