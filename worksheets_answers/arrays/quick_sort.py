


"""
given an array
sort it using quick sort. 
return the count of swaps. 
"""

def quick_s(arr, low, high):
    if low < high:
        pivot = arr[high]

        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        quick_s(arr, low, i)
        quick_s(arr, i + 2, high)


def quick_sort(arr):
    quick_s(arr, 0, len(arr)-1)
    