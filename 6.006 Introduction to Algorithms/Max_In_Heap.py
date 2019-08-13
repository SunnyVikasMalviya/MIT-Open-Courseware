from Build_Max_Heap import build_max_heap

def max_in_heap(arr) :
    """
    The max_in_heap function returns the maximum valued element from a heap by
    making a max_heap using the build_max_heap function.
    """
    arr = build_max_heap(arr)
    return arr[0]


#For Debugging
#print(max_in_heap([1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
INPUT

[1, 2, 3, 4, 5, 6, 7, 8, 9]

OUTPUT

9
"""
