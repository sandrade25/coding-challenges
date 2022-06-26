import pytest
import sys


sys.path.append("../../")
import random


from protected.worksheets_answers.c_sorting.insertion_sort import insertion_sort as insertion_sort_a
from worksheets.c_sorting.insertion_sort import insertion_sort
from protected.worksheets_answers.c_sorting.merge_sort import merge_sort as merge_sort_a
from worksheets.c_sorting.merge_sort import merge_sort
from protected.worksheets_answers.c_sorting.quick_sort import quick_sort as quick_sort_a
from worksheets.c_sorting.quick_sort import quick_sort
from protected.worksheets_answers.c_sorting.heap_sort import heap_sort as heap_sort_a
from worksheets.c_sorting.heap_sort import heap_sort

class TestSorting:
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

        merge_sort_a(l1)
        
        assert l1_a == l1

        test = merge_sort(l2)
        assert test != "not implemented", "solution not yet provided"
        assert l2_a == l2

        assert l1 == l2

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

        quick_sort_a(l1)
        assert l1_a == l1

        test = quick_sort(l2)
        assert test != "not implemented", "solution not yet provided"
        assert l2_a == l2

        assert l2 == l1

    
    def test_heap_sort(self, unsorted_list):
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

        heap_sort_a(l1)
        assert l1_a == l1

        test = heap_sort(l2)
        assert test != "not implemented", "solution not yet provided"
        assert l2_a == l2

        assert l2 == l1








