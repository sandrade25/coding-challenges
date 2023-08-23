import sys
sys.path.append("../../")
from protected.useables.linked_node import LinkedNode


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

    
    new_node = LinkedNode(data=data, next_node=node)
    if prev_node:
        prev_node.next = new_node
    else:
        llist.head = new_node

    return llist



    