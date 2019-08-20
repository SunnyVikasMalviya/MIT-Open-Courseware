from Build_Max_Heap import build_max_heap

def heap_sort_desc(arr) :
    brr = []
    n = len(arr)
    #print(type(arr))
    for x in range(n) :
        arr = build_max_heap(arr)
        #print(arr)
        arr[-1], arr[0] = arr[0], arr[-1]
        brr.append(arr[-1])
        arr.remove(arr[-1])
    return brr

def heap_sort_asc(arr) :
    arr = heap_sort_desc(arr)
    return reversed(arr)

#For Debugging
if __name__ == "__main__" :
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [print(x, end=" ") for x in heap_sort_desc(arr)]
    print(type(heap_sort_desc(arr)))
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [print(x, end=" ") for x in heap_sort_asc(arr)]
    print(type(heap_sort_asc(arr)))
