def counting_sort(arr) :
    """
    The counting_sort takes a list of integers in unsorted order and returns a
    sorted list.
    It first creates a list of counters set at zero initially, for elements starting
    from 0 to max of the list. Then it iterates through each of the element in
    given list and keeps incrementing the counter at that index by one as soon as
    the element arrives. At the end, it creates a new list of the index(representing
    list element) res, which has the element counter times and extends the res list.
    Time Complexity : O(nlogn)
    It takes only one argument:
    arr : unsorted list of integers
    It returns a sorted list(named res) having the same length as the arr.
    """
    brr = []
    brr = [0 for x in range(max(arr)+1)]
    #print(brr)
    #The above line makes a list till max+1 of arr.
    #The list will store the counter of each integer in arr.
    #The enum part of list will be used as the for each unique element in arr.
    for x in arr :
        brr[x] += 1
    res = []
    for x in range(len(brr)) :
        res.extend(x for y in range(brr[x]))
        #print(res)      #For Debugging
    return res
        
    

if __name__ == '__main__' :
    arr = [2, 5, 3, 8, 2, 9, 0, 3, 5, 6, 8, 9, 5, 9, 8, 0, 2, 5, 5, 6, 5]
    print(counting_sort(arr))


"""
INPUT

[2, 5, 3, 8, 2, 9, 0, 3, 5, 6, 8, 9, 5, 9, 8, 0, 2, 5, 5, 6, 5]    #This is arr

OUTPUT (With debugging part)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    #This is brr
[0, 0]                            #From here, its res
[0, 0]
[0, 0, 2, 2, 2]
[0, 0, 2, 2, 2, 3, 3]
[0, 0, 2, 2, 2, 3, 3]
[0, 0, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5]
[0, 0, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6]
[0, 0, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6]
[0, 0, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6, 8, 8, 8]
[0, 0, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6, 8, 8, 8, 9, 9, 9]
[0, 0, 2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6, 8, 8, 8, 9, 9, 9]

"""
