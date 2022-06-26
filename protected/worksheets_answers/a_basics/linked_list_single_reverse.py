


"""
given a linked list,
reverse it 
"""

def reverse_single_linked_list(llist):
    node = llist.head
    prev_node = None
    while node:
        next = node.next
        node.next = prev_node
        prev_node = node
        node = next
    llist.head = prev_node
    return llist