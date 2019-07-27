from Two_Finger_Sort import two_finger_sort

def merge_sort(arr):
    """
    The merge_sort function takes one unsorted list as argument and returns the
    sorted list. It uses a divide and conquer algorithm.
    It divides the list by recursively calling merge_sort with half of the list. 
    It uses the two_finger_sort function to sort and conquer the list parts.
    """
    if len(arr) == 1:
        return arr
    else :
        n = len(arr)
        return two_finger_sort(merge_sort(arr[0:n//2]), merge_sort(arr[n//2:]))

#For Debugging
#print(merge_sort([3, 7, 2, 1, 6, 5]))



"""
INPUT

[3, 7, 2, 1, 6, 5]

OUTPUT

[1, 2, 3, 5, 6, 7]


INPUT

[3, 7, 2, 1, 6, 5, 5, 6, 8, 9, 6, 0.8]

OUTPUT

[0.8, 1, 2, 3, 5, 5, 6, 6, 6, 7, 8, 9]
"""
