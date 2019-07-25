def insertion_sort(arr):
    """
    The function insertion_sort() sorts the given list using insertion sort algorithm.
    The function returns the list after sorting it.
    Arguments
    arr : An unsorted list.
    """
    for x in arr[1:]:
        for y in arr[arr.index(x)-1::-1]:
            if x < y:
                arr[arr.index(x)] = y
                arr[arr.index(y)] = x                                
    return arr
                
            
#for debugging
#arr = [5, 3, 4, 6, 1, 2]
#arr = []
#arr = input().split(' ')
#arr = [int(x) for x in arr]    #DATA CONVERSION LINE 
#print(insertion_sort(arr))


"""
INPUT

7 5 0 9 8


OUTPUT

With DATA CONVERSION LINE
[0, 5, 7, 8, 9]

Without DATA CONVERSION LINE
['0', '5', '7', '8', '9']
"""
