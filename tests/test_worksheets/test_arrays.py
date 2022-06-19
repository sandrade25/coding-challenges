import pytest
import sys
sys.path.append("../../")
import random
from worksheets_answers.arrays.binary_search import binary_search as binary_search_a
from worksheets.arrays.binary_search import binary_search
from worksheets_answers.arrays.insertion_sort import insertion_sort as insertion_sort_a
from worksheets.arrays.insertion_sort import insertion_sort
from worksheets_answers.arrays.merge_sort import merge_sort as merge_sort_a
from worksheets.arrays.merge_sort import merge_sort
from worksheets_answers.arrays.quick_sort import quick_sort as quick_sort_a
from worksheets.arrays.quick_sort import quick_sort

class TestArrays:
    def test_binary_search(self, sorted_list):
        choice_1 = random.randint(250,300)
        choice_2 = random.randint(0,100)
        choice_3 = random.randint(75,250)
        
        randomized_sorted_list = random.choices(sorted_list, k=50)
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
        assert user2 == answer2
        assert user3 == answer3
        assert user4 == answer4
    
    def test_insertion_sort(self, unsorted_list):
        l1 = unsorted_list.copy()
        l1_a = l1.copy()
        l1_a.sort()

        l2 = unsorted_list.copy()
        l2_a = l2.copy()
        l2_a.sort()

        assert l1 == l2
        assert l1_a != l1
        assert l2_a != l2
        assert l2_a == l1_a

        answer = insertion_sort_a(l1)
        assert l1_a == l1

        user = insertion_sort(l2)
        assert user is not None, "solution not yet provided"
        assert l2_a == l2

        assert answer == user

    def test_merge_sort(self, unsorted_list):
        l1 = unsorted_list.copy()
        l1_a = l1.copy()
        l1_a.sort()

        l2 = unsorted_list.copy()
        l2_a = l2.copy()
        l2_a.sort()

        assert l1 == l2
        assert l1_a != l1
        assert l2_a != l2
        assert l2_a == l1_a

        answer = merge_sort_a(l1)
        assert l1_a == l1

        user = merge_sort(l2)
        assert user is not None, "solution not yet provided"
        assert l2_a == l2

        assert answer == user

    def test_quick_sort(self, unsorted_list):
        l1 = unsorted_list.copy()
        l1_a = l1.copy()
        l1_a.sort()

        l2 = unsorted_list.copy()
        l2_a = l2.copy()
        l2_a.sort()

        assert l1 == l2
        assert l1_a != l1
        assert l2_a != l2
        assert l2_a == l1_a

        answer = quick_sort_a(l1)
        assert l1_a == l1

        user = quick_sort(l2)
        assert user is not None, "solution not yet provided"
        assert l2_a == l2

        assert answer == user

    def test_array_manipulation(self):
        raise NotImplementedError

    def test_minimum_swaps(self):
        raise NotImplementedError

    def test_two_d_array(self):
        raise NotImplementedError

    





