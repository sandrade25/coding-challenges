import sys
sys.path.append("../../")
from useables.linked_node import LinkedNode


"""
given a linked list,
insert an element at position and ensure linked list is intact.
"""

def insert_linked_list(llist, position, data):
    node = llist.head
    curr_position = 0
    prev_node = None
    while node and curr_position < position:
        prev_node = node
        node = node.next
        curr_position += 1

    if curr_position == position and node:
        new_node = LinkedNode(data=data, next_node=node)
        prev_node.next = new_node

    return llist



    