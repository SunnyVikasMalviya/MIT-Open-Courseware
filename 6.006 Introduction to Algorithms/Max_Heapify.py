def max_heapify(arr, i, n) :
    """
    The max_heapify function makes a max heap out of a heap that has a single
    violation of the max heap property.
    The list should be have odd number of elements in order to visualize it as
    a nearly complete binary tree.
    Time complexity of max_heapify is O(log n)
    ***
    Assumption
    Taking the violation element i as the root, the left child and right child
    should be max_heaps.
    ***
    It takes three arguments.
    arr = list of elements
    i = index at which the max heap property is violated.
    n = number of elements in the list.
    """
    if n % 2 != 1:
        return "Number of elements should be odd in order to visualize the list heap as a binary tree."
    if arr[i] < arr[(2*i)+1] or arr[i] < arr[(2*i)+2] :
        if arr[(2*i)+1] >= arr[(2*i)+2]:
            arr[(2*i)+1], arr[i] = arr[i], arr[(2*i)+1]
            if n//2 > (2*i)+1:
                max_heapify(arr, (2*i)+1, n)
        else :
            arr[(2*i)+2], arr[i] = arr[i], arr[(2*i)+2]
            if n//2 > (2*i)+2 :
                max_heapify(arr, (2*i)+2, n)
    return arr



#For Debugging
#print(max_heapify([9, 1, 8, 4, 5, 6, 7, 3, 2], 1, 9))


"""
INPUT

[9, 1, 8, 4, 5, 6, 7, 3, 2]
OUTPUT

[9, 5, 8, 4, 1, 6, 7, 3, 2]
"""
