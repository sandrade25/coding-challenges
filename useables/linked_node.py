

class LinkedNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class DoubleLinkedNode:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.prev = previous_node
        self.next = next_node