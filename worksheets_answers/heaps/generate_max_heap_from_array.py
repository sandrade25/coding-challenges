


"""
given an array. generate a complete binary tree max heap
return a heapified array.
"""


def heapify(arr, i):
    # i == root node of tree section we are looking at.
    n = len(arr)
    largest = i # initialize largest as root

    l = 2 * i + 1 # left leaf node = 2*i + 1
    r = 2 * i + 2 # right leaf node

    #  if left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l 
    
    # if right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursivly heapify the affected sub-tree
        heapify(arr, largest)

def generate_max_heap_from_array(arr):
    last_parent_node_index = len(arr) // 2 - 1

    # working from the last parent node, heapify each section of tree within array
    for i in range(last_parent_node_index, -1, -1):
        heapify(arr, i)