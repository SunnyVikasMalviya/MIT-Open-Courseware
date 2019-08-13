from Max_Heapify import max_heapify

def build_max_heap(arr) :
    """
    Heap data structures are lists that are visualized as nearly complete binary
    trees.
    A max heap is the list whose tree has all parent nodes having higher values
    than its children nodes.
    The build_max_heap function takes a list of unordered elements and returns
    a max heap.
    The time complexity of build_max_heap() is O(n).
    It takes a single argument.
    arr : unordered list of element.
    """
    n = len(arr)
    if n % 2 != 1:
        return "Number of elements in your list should be odd in order to \
visualize it as a heap."
    for i in reversed(range(n//2)) :
        arr = max_heapify(arr, i, n)
    return arr

#For Debugging
#print(build_max_heap([1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
INPUT

[1, 2, 3, 4, 5, 6, 7, 8, 9]

OUTPUT

[9, 8, 7, 4, 5, 6, 3, 2, 1]
"""
