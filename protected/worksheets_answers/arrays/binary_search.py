
"""
find a given element (ele)
with a sorted array (arr)

return True if found. and what position. 
return False, None if not found
"""

def bsearch(arr, start, end, ele):
    if start >= end:
        if arr[end] == ele:
            return True, end
        else:
            return False, None

    mid = ((end - start) // 2) + start

    if arr[mid] == ele:
        return True, mid
    
    elif arr[mid] > ele:
        return bsearch(arr, start, mid-1, ele)
    
    elif arr[mid] < ele:
        return bsearch(arr, mid+1, end, ele)
    




def binary_search(arr, ele):
    return bsearch(arr, 0, len(arr)-1, ele)
    

    