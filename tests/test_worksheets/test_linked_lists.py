from pkgutil import get_data
import pytest
import sys
sys.path.append("../../")
import random
from worksheets.linked_lists.delete_double_linked_list import delete_double_linked_list
from worksheets.linked_lists.delete_single_linked_list import delete_linked_list
from worksheets.linked_lists.insert_double_linked_list import insert_double_linked_list
from worksheets.linked_lists.insert_single_linked_list import insert_linked_list
from worksheets.linked_lists.reverse_double_linked_list import reverse_double_linked_list
from worksheets.linked_lists.reverse_single_linked_list import reverse_single_linked_list
from protected.worksheets_answers.linked_lists.delete_double_linked_list import delete_double_linked_list as delete_double_linked_list_a
from protected.worksheets_answers.linked_lists.delete_single_linked_list import delete_linked_list as delete_linked_list_a
from protected.worksheets_answers.linked_lists.insert_double_linked_list import insert_double_linked_list as insert_double_linked_list_a
from protected.worksheets_answers.linked_lists.insert_single_linked_list import insert_linked_list as insert_linked_list_a
from protected.worksheets_answers.linked_lists.reverse_double_linked_list import reverse_double_linked_list as reverse_double_linked_list_a
from protected.worksheets_answers.linked_lists.reverse_single_linked_list import reverse_single_linked_list as reverse_single_linked_list_a

def get_data_order(llist):
    order = []
    node = llist.head
    while node:
        order.append(node.data)
        node = node.next
    return order


class TestLinkedLists:
    def test_delete_double_linked_list(self, double_linked_list):
        original_order = get_data_order(double_linked_list)
        answer1 = delete_double_linked_list_a(double_linked_list, 100)
        answer1_order = get_data_order(answer1)
        assert answer1_order == original_order

        answer2 = delete_double_linked_list_a(double_linked_list, 5)
        answer2_order = get_data_order(answer2)
        answer2.revert()

        user_answer1 = delete_double_linked_list(double_linked_list, 100)
        assert user_answer1 is not None, "solution not yet provided"

        user_answer1_order = get_data_order(user_answer1)

        user_answer2 = delete_double_linked_list(double_linked_list, 5)
        user_answer2_order = get_data_order(user_answer2)
        user_answer2.revert()

        assert user_answer1_order == answer1_order
        assert user_answer2_order == answer2_order
        
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

        user_answer1 = insert_linked_list(linked_list, 100, 1111)
        assert user_answer1 is not None, "solution not yet provided"

        user_answer1_order = get_data_order(user_answer1)

        user_answer2 = insert_linked_list(linked_list, 5, 1111)
        user_answer2_order = get_data_order(user_answer2)
        user_answer2.revert()

        assert user_answer1_order == answer1_order
        assert user_answer2_order == answer2_order

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


    





