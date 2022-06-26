import pytest
import sys


sys.path.append("../../")
import random
from protected.worksheets_answers.c_search.binary_search import binary_search as binary_search_a
from worksheets.c_search.binary_search import binary_search


class TestSearch:
    def test_binary_search(self, sorted_list):
        choice_1 = random.randint(250,300)
        choice_2 = random.randint(0,100)
        choice_3 = random.randint(75,250)
        
        randomized_sorted_list = list(set(random.choices(sorted_list, k=50)))
        randomized_sorted_list.sort()
        choice_4 = random.choice(randomized_sorted_list)

        answer1 = binary_search_a(sorted_list, choice_1)
        answer2 = binary_search_a(sorted_list, choice_2)
        answer3 = binary_search_a(sorted_list, choice_3)
        answer4 = binary_search_a(randomized_sorted_list, choice_4)

        user1 = binary_search(sorted_list, choice_1)
        user2 = binary_search(sorted_list, choice_2)
        user3 = binary_search(sorted_list, choice_3)
        user4 = binary_search(randomized_sorted_list, choice_4)

        assert user1 is not None, "solution not yet provided"

        assert user1 == answer1
        if user1[0]:
            assert sorted_list[user1[1]] == choice_1

        assert user2 == answer2
        if user2[0]:
            assert sorted_list[user2[1]] == choice_2

        assert user3 == answer3
        if user3[0]:
            assert sorted_list[user3[1]] == choice_3

        assert user4 == answer4
        if user4[0]:
            assert randomized_sorted_list[user4[1]] == choice_4
    

    



