import pytest
import sys


sys.path.append("../../")
import random

from worksheets.e_algo_2.roads_and_libraries import roads_and_libraries
from protected.worksheets_answers.e_algo_2.roads_and_libraries import roads_and_libraries as roads_and_libraries_a
from worksheets.e_algo_2.dfs_word_in_board import dfs_word_in_board
from protected.worksheets_answers.e_algo_2.dfs_word_in_board import dfs_word_in_board as dfs_word_in_board_a
from worksheets.e_algo_2.depth_first_cycle import depth_first_cycle
from protected.worksheets_answers.e_algo_2.depth_first_cycle import depth_first_cycle as depth_first_cycle_a
from worksheets.e_algo_2.bfs_shortest_reach_in_graph import  bfs_shortest_reach_in_graph
from protected.worksheets_answers.e_algo_2.bfs_shortest_reach_in_graph import  bfs_shortest_reach_in_graph as bfs_shortest_reach_in_graph_a

class TestAlgo2:
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




