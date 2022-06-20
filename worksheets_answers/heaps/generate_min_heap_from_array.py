


"""
given an array. generate a complete binary tree min heap
return a heapified array

recall that you must work from the last parent node and its following leaf nodes and heapify upwards. 

"""

def heapify(arr, i):
    # i == root node of tree section we are looking at.
    n = len(arr)
    smallest = i # initialize smallest as root

    l = 2 * i + 1 # left leaf node = 2*i + 1
    r = 2 * i + 2 # right leaf node

    #  if left child is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l 
    
    # if right child is smaller than smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # if smallest is not root
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        # recursivly heapify the affected sub-tree
        heapify(arr, smallest)

def generate_min_heap_from_array(arr):
    last_parent_node_index = len(arr) // 2 - 1

    # working from the last parent node, heapify each section of tree within array
    for i in range(last_parent_node_index, -1, -1):
        heapify(arr, i)