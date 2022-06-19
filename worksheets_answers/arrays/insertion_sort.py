


"""
given an array
sort it using insertion sort. 
count how many swaps take place. 
return the count of swaps. 
"""

def insertion_sort(arr):
    count_of_swaps = 0
    for i in range(len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            count_of_swaps += 1
            j -= 1
        arr[j+1] = key
    return count_of_swaps