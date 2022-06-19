


"""
given a double linked list,
reverse it
"""

def reverse_double_linked_list(llist):
    node = llist.head

    prev_node = None
    while node:
        next = node.next
        prev = node.prev
        node.next = prev
        node.prev = next
        prev_node = node
        node = next

    
    llist.head = prev_node
    return llist