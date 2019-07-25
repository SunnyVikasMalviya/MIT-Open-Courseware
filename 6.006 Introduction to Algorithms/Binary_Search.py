def binary_search(arr, first, last, element):
    """
    Function to search an element in a given sorted list.
    The function returns the index of the first occurrence of an element in the list.
    If the element is not present, it returns -1.
    Arguments
    arr : list of elements
    first : position of the first element
    last : position of the last element
    element : element that is to be searched
    """
    mid = (first + last) // 2
    if first <= last:
        if element == arr[mid]:
            return arr.index(element)
        elif element > arr[mid]:
            return binary_search(arr, mid+1, last, element)
        elif element < arr[mid]:
            return binary_search(arr, first, mid-1, element)
    else:
        return -1


#arr = []
#n = int(input("Enter number of elements:"))
#arr = sorted([int(input()) for x in range(n)])
#element = int(input("Enter element to be searched:"))
#print("Sorted list: ", arr)
#print("Index of the element {} in list is {}".format(element, binary_search(arr, 0, n-1, element)))    
#The below line prints the docstring of the function binary_search()
#help(binary_search)
