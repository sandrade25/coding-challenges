import pytest
import sys
sys.path.append("../../")
from useables.linked_node import DoubleLinkedList, LinkedNode, DoubleLinkedNode, LinkedList
import random

@pytest.fixture(scope="function")
def word_board():
    return [
        ['c', 'o', 'b', 'b', 'c', 'r',],
        ['r', 'r', 'r', 'k', 'p', 'e',],
        ['u', 'p', 'a', 'p', 'e', 'a',],
        ['p', 'o', 'n', 'f', 'l', 't',],
        ['t', 'i', 'r', 'p', 'o', 'e',],
    ], ["corruption", "flea", "pole", "cobb", "create", "pea", "flop", "poe", "ape", "eat", "ate", "park", "bran", "nape", "pan"]



@pytest.fixture(scope="function")
def binary_grid1():
    return [[0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

@pytest.fixture(scope="function")
def binary_grid2():
    return [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]


@pytest.fixture(scope="function")
def binary_grid3():
    return [[1, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 0, 1], [1, 1, 1, 0, 0]]


@pytest.fixture(scope="function")
def binary_grid4():
    return [
        [1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0]
        ]




