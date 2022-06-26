import sys
sys.path.append("../../")
from protected.useables.linked_node import LinkedNode



"""
given a linked list,
delete an element at position and ensure linked list is intact.
"""

def delete_linked_list(llist, position):
    node = llist.head
    curr_position = 0
    prev_node = None

    while node and curr_position < position:
        prev_node = node
        node = node.next
        curr_position += 1

    if curr_position == position and node:
        next = node.next
        prev_node.next = next

    return llist