import sys
sys.path.append("../../")
from useables.linked_node import DoubleLinkedNode



"""
given a double linked list,
delete an element at position and ensure linked list is intact.
"""

def delete_double_linked_list(llist, position):
    node = llist.head
    curr_position = 0
    prev_node = None

    while node and curr_position < position:
        prev_node = node
        node = node.next

    if curr_position == position and node:
        next = node.next
        prev_node.next  = next
        next.prev = prev_node

    return llist
    
