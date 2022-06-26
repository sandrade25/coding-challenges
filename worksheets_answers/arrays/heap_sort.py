"""
sort algorithm using heap sort.

"""

def heapify(arr, i, max_ind):
    # i == root node of tree section we are looking at.
    n = len(arr)
    largest = i # initialize largest as root

    l = 2 * i + 1 # left leaf node = 2*i + 1
    r = 2 * i + 2 # right leaf node

    #  if left child is larger than root
    if l <= max_ind and arr[l] > arr[largest]:
        largest = l 
    
    # if right child is larger than largest so far
    if r <= max_ind and arr[r] > arr[largest]:
        largest = r

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursivly heapify the affected sub-tree
        heapify(arr, largest, max_ind)

def generate_max_heap_from_array(arr, max_len):
    last_parent_node_index = max_len // 2 - 1

    # working from the last parent node, heapify each section of tree within array
    for i in range(last_parent_node_index, -1, -1):
        heapify(arr, i, max_len-1)

def heap_sort(arr):
    n = len(arr)

    for new_len in range(n, 0, -1):
        generate_max_heap_from_array(arr, new_len)
        arr[new_len-1], arr[0] = arr[0], arr[new_len-1]



if __name__ == "__main__":
    l = [0,5,10,9,3,1,6,2,8,7,11,21,50]
    heap_sort(l)

