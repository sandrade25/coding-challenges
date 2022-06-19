

class LinkedNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class DoubleLinkedNode:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.prev = previous_node
        self.next = next_node


class LinkedList:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.revert()
        

    def revert(self):
        self.head = None
        prev_node = None
        for i in range(self.size):
            node = LinkedNode(data=i)

            if not self.head:
                self.head = node

            if prev_node:
                prev_node.next = node

            prev_node = node


class DoubleLinkedList:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.revert()

    def revert(self):
        self.head = None
        prev_node = None
        for i in range(self.size):
            node = DoubleLinkedNode(data=i, previous_node=prev_node)

            if not self.head:
                self.head = node

            if prev_node:
                prev_node.next = node

            prev_node = node

