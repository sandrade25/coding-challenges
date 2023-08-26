import pytest
import sys


sys.path.append("../../")
import random

from worksheets.a_basics.calculate_fibonnaci import fibonnaci
from worksheets.a_basics.tri_make_from_words import make_trie
from worksheets.a_basics.tri_get_words_from import get_words_from_trie
from protected.worksheets_answers.a_basics.calculate_fibonnaci import fibonnaci as fibonnaci_a
from protected.worksheets_answers.a_basics.tri_make_from_words import make_trie as make_trie_a
from protected.worksheets_answers.a_basics.tri_get_words_from import get_words_from_trie as get_words_from_trie_a

from worksheets.a_basics.linked_list_double_delete import delete_double_linked_list
from worksheets.a_basics.linked_list_single_delete import delete_linked_list
from worksheets.a_basics.linked_list_double_insert import insert_double_linked_list
from worksheets.a_basics.linked_list_single_insert import insert_linked_list
from worksheets.a_basics.linked_list_double_reverse import reverse_double_linked_list
from worksheets.a_basics.linked_list_single_reverse import reverse_single_linked_list
from protected.worksheets_answers.a_basics.linked_list_double_delete import delete_double_linked_list as delete_double_linked_list_a
from protected.worksheets_answers.a_basics.linked_list_single_delete import delete_linked_list as delete_linked_list_a
from protected.worksheets_answers.a_basics.linked_list_double_insert import insert_double_linked_list as insert_double_linked_list_a
from protected.worksheets_answers.a_basics.linked_list_single_insert import insert_linked_list as insert_linked_list_a
from protected.worksheets_answers.a_basics.linked_list_double_reverse import reverse_double_linked_list as reverse_double_linked_list_a
from protected.worksheets_answers.a_basics.linked_list_single_reverse import reverse_single_linked_list as reverse_single_linked_list_a
from protected.worksheets_answers.a_basics.heap_generate_max import generate_max_heap_from_array as generate_max_heap_from_array_a
from protected.worksheets_answers.a_basics.heap_generate_min import generate_min_heap_from_array as generate_min_heap_from_array_a

from worksheets.a_basics.heap_generate_max import generate_max_heap_from_array
from worksheets.a_basics.heap_generate_min import generate_min_heap_from_array

def get_data_order(llist):
    order = []
    node = llist.head
    while node:
        order.append(node.data)
        node = node.next
    return order


class TestBasics:
    def test_fibonacci(self):
        assert fibonnaci(5) is not None, "solution not yet provided"

        assert fibonnaci_a(5) is not None
        assert fibonnaci(0) == fibonnaci_a(0) == 0
        assert fibonnaci(1) == fibonnaci_a(1) == 1
        assert fibonnaci(2) == fibonnaci_a(2) == 1
        assert fibonnaci(10) == fibonnaci_a(10)
        assert fibonnaci(20) == fibonnaci_a(20)
        assert fibonnaci(79) == fibonnaci_a(79)

    def test_make_trie(self, list_of_words):
        random_list_1 = random.choices(list_of_words, k=10)
        random_list_2 = random.choices(list_of_words, k=10)
        random_list_3 = random.choices(list_of_words, k=10)
        assert make_trie(random_list_1) is not None, "solution not yet provided"

        assert make_trie_a(random_list_1) is not None
        assert make_trie(random_list_1) == make_trie_a(random_list_1)
        assert make_trie(random_list_2) == make_trie_a(random_list_2)
        assert make_trie(random_list_3) == make_trie_a(random_list_3)

    def test_get_words_from_trie(self, trie):
        user = get_words_from_trie(trie)
        answer = get_words_from_trie_a(trie)
        assert user is not None, "solution not yet provided"

        assert answer is not None
        assert user == answer

    def test_delete_double_linked_list(self, double_linked_list):
        original_order = get_data_order(double_linked_list)
        answer1 = delete_double_linked_list_a(double_linked_list, 100)
        answer1_order = get_data_order(answer1)
        assert answer1_order == original_order

        answer2 = delete_double_linked_list_a(double_linked_list, 5)
        answer2_order = get_data_order(answer2)
        answer2.revert()

        answer3 = delete_double_linked_list_a(double_linked_list, 0)
        answer3_order = get_data_order(answer3)
        answer3.revert()

        user_answer1 = delete_double_linked_list(double_linked_list, 100)
        assert user_answer1 is not None, "solution not yet provided"

        user_answer1_order = get_data_order(user_answer1)

        user_answer2 = delete_double_linked_list(double_linked_list, 5)
        user_answer2_order = get_data_order(user_answer2)
        user_answer2.revert()

        user_answer3 = delete_double_linked_list(double_linked_list, 0)
        user_answer3_order = get_data_order(user_answer3)
        user_answer3.revert()
        
        assert user_answer1_order == answer1_order
        assert user_answer2_order == answer2_order
        assert user_answer3_order == answer3_order
        
    def test_delete_linked_list(self, linked_list):
        original_order = get_data_order(linked_list)
        answer1 = delete_linked_list_a(linked_list, 100)
        answer1_order = get_data_order(answer1)
        assert answer1_order == original_order

        answer2 = delete_linked_list_a(linked_list, 5)
        answer2_order = get_data_order(answer2)
        answer2.revert()

        user_answer1 = delete_linked_list(linked_list, 100)
        assert user_answer1 is not None, "solution not yet provided"

        user_answer1_order = get_data_order(user_answer1)

        user_answer2 = delete_linked_list(linked_list, 5)
        user_answer2_order = get_data_order(user_answer2)
        user_answer2.revert()

        assert user_answer1_order == answer1_order
        assert user_answer2_order == answer2_order

    def test_insert_double_linked_list(self, double_linked_list):
        original_order = get_data_order(double_linked_list)
        answer1 = insert_double_linked_list_a(double_linked_list, 100, 1111)
        answer1_order = get_data_order(answer1)
        assert answer1_order == original_order + [1111]

        answer2 = insert_double_linked_list_a(double_linked_list, 5, 1111)
        answer2_order = get_data_order(answer2)
        answer2.revert()

        answer3 = insert_double_linked_list_a(double_linked_list, 0, 1111)
        answer3_order = get_data_order(answer3)
        answer3.revert()

        user_answer1 = insert_double_linked_list(double_linked_list, 100, 1111)
        assert user_answer1 is not None, "solution not yet provided"

        user_answer1_order = get_data_order(user_answer1)

        user_answer2 = insert_double_linked_list(double_linked_list, 5, 1111)
        user_answer2_order = get_data_order(user_answer2)
        user_answer2.revert()

        user_answer3 = insert_double_linked_list(double_linked_list, 0, 1111)
        user_answer3_order = get_data_order(user_answer3)
        user_answer3.revert()

        assert user_answer1_order == answer1_order
        assert user_answer2_order == answer2_order
        assert answer3_order == user_answer3_order
        assert answer3_order[0] == 1111
        assert user_answer3_order[0] == 1111

    def test_insert_linked_list(self, linked_list):
        original_order = get_data_order(linked_list)
        answer1 = insert_linked_list_a(linked_list, 100, 1111)
        answer1_order = get_data_order(answer1)
        assert answer1_order == original_order + [1111]

        answer2 = insert_linked_list_a(linked_list, 5, 1111)
        answer2_order = get_data_order(answer2)
        answer2.revert()

        answer3 = insert_linked_list_a(linked_list, 0, 1111)
        answer3_order = get_data_order(answer3)
        answer3.revert()

        user_answer1 = insert_linked_list(linked_list, 100, 1111)
        assert user_answer1 is not None, "solution not yet provided"

        user_answer1_order = get_data_order(user_answer1)

        user_answer2 = insert_linked_list(linked_list, 5, 1111)
        user_answer2_order = get_data_order(user_answer2)
        user_answer2.revert()

        user_answer3 = insert_linked_list(linked_list, 0, 1111)
        user_answer3_order = get_data_order(user_answer3)
        user_answer3.revert()

        assert user_answer1_order == answer1_order
        assert user_answer2_order == answer2_order
        assert user_answer3_order == answer3_order

    def test_reverse_double_linked_list(self, double_linked_list):
        original_order = get_data_order(double_linked_list)
        answer = reverse_double_linked_list_a(double_linked_list)
        new_order_answer = get_data_order(answer)
        reverse_double_linked_list_a(double_linked_list)

        user = reverse_double_linked_list(double_linked_list)
        assert user is not None, "solution not yet provided"

        new_order_user = get_data_order(user)

        assert new_order_user == new_order_answer
        assert new_order_user != original_order
        original_order.reverse()
        assert new_order_user == original_order

    def test_reverse_single_linked_list(self, linked_list):
        original_order = get_data_order(linked_list)
        answer = reverse_single_linked_list_a(linked_list)
        new_order_answer = get_data_order(answer)
        reverse_single_linked_list_a(linked_list)

        assert original_order == get_data_order(linked_list)

        user = reverse_single_linked_list(linked_list)
        assert user is not None, "solution not yet provided"

        new_order_user = get_data_order(user)

        assert new_order_user == new_order_answer
        assert new_order_user != original_order
        original_order.reverse()
        assert new_order_user == original_order


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
            



