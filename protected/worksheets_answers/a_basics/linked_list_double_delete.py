import sys
sys.path.append("../../")
from protected.useables.linked_node import DoubleLinkedNode



"""
given a double linked list,
delete an element at position and ensure linked list is intact.
"""

def delete_double_linked_list(llist, position):
    node = llist.head
    curr_position = 0
    prev_node = None

    while node.next and curr_position < position:
        prev_node = node
        node = node.next
        curr_position += 1

    if curr_position == position:
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            llist.head = next_node
            next_node.prev = None
        del node

    return llist
