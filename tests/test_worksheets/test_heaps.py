import pytest
import sys
sys.path.append("../../")
import random
from worksheets_answers.heaps.generate_max_heap_from_array import generate_max_heap_from_array as generate_max_heap_from_array_a
from worksheets_answers.heaps.generate_min_heap_from_array import generate_min_heap_from_array as generate_min_heap_from_array_a
from worksheets_answers.heaps.max_heap_remove_item import max_heap_remove_item as max_heap_remove_item_a
from worksheets_answers.heaps.min_heap_remove_item import min_heap_remove_item as min_heap_remove_item_a

from worksheets.heaps.generate_max_heap_from_array import generate_max_heap_from_array
from worksheets.heaps.generate_min_heap_from_array import generate_min_heap_from_array


class TestHeaps:
    def test_generate_max_heap_from_array(self, unsorted_list):
        answer1 = unsorted_list.copy()
        user1 = unsorted_list.copy()
        original = answer1.copy()

        assert user1 == answer1
        generate_max_heap_from_array_a(answer1)
        assert original != answer1
        t = generate_max_heap_from_array(user1)
        assert t != "Not implemented", "solution not yet provided"
        assert user1 == answer1
        
    def test_generate_min_heap_from_array(self, unsorted_list):
        answer1 = unsorted_list.copy()
        user1 = unsorted_list.copy()
        original = answer1.copy()

        assert user1 == answer1
        generate_min_heap_from_array_a(answer1)
        assert original != answer1
        t = generate_min_heap_from_array(user1)
        assert t != "Not implemented", "solution not yet provided"
        assert user1 == answer1
        
        

    





