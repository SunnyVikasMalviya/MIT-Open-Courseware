from Counting_Sort import counting_sort

def radix_sort(arr) :
    """
    radix_sort takes in a list of integers and arranges the numbers in ascending
    order using counting_sort() on digits of each of these numbers starting
    from once to tens to hundreds ... till the left most digit and gets the
    numbers sorted.
    Arguments
    arr : list of unsorted integers
    Returns
    res : sorted list
    """
    temp = []
    div1 = 10
    div2 = 1
    times = len(str(max(arr)))
    while times > 0 :
        for x in arr :
            temp.append((x%div1)//div2)
        temp = counting_sort(temp)
        for i in temp :
            for j in arr :
                if i == (j%div1)//div2 :
                    arr.remove(j)
                    arr.append(j)
                    break
        div1 *= 10
        div2 *= 10
        times -=1
        temp.clear()
        #print(arr)
    return arr
    
if __name__ == '__main__' :
    arr = [129, 2, 47, 334, 678, 345, 989, 687, 524, 864, 76, 544]
    print(radix_sort(arr))


"""
INPUT

[129, 2, 47, 334, 678, 345, 989, 687, 524, 864, 76, 544]

OUTPUT

[2, 47, 76, 129, 334, 345, 524, 544, 678, 687, 864, 989]
"""
