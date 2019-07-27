def two_finger_sort(arr, brr):
    """
    The two_finger_sort() is a function that takes two sorted lists as input
    parameters and returns a single sorted list.
    Its time complexity is O(n), but it also needs extra space to store the new
    sorted list.
    Explanation : arr = [1, 2, 34, 56], brr = [3, 5], crr = []
                         ^                     ^
    1. Compare the elements that are at the beginning i.e. arr[0] and brr[0].
    2. Choose the smaller element and copy it to a new list i.e. arr[0] in this case.
    3. Move the pointer to the next element i.e. arr[1] in this case.
    4. Compare again and then move to step 2.
    5. Complete the comparison till one of the lists is exhausted with the elements
       and then copy the rest of the elements in the other list to the list crr.
    6. Return the crr list.

    crr = [1, 2, 3, 5, 34, 56]
    """
    if arr == sorted(arr) and brr == sorted(brr):
        i = 0
        j = 0
        crr = []
        while i < len(arr) and j < len(brr):
            if arr[i] > brr[j]:
                crr.append(brr[j])
                j = j + 1
            elif arr[i] == brr[j]:
                crr.append(arr[i])
                crr.append(brr[j])
                i = i + 1
                j = j + 1
            else :
                crr.append(arr[i])
                i = i + 1
        if i == len(arr):
            while j < len(brr):
                crr.append(brr[j])
                j = j + 1
        else :
            while i < len(arr):
                crr.append(arr[i])
                i = i + 1
        return crr
    else :
        return "Error : The input lists should be sorted."
            

#For Debugging
#print(two_finger_sort([1, 2, 3, 4, 56], [3, 5]))

"""
INPUT

arr = [1, 2, 34, 56]
brr = [3, 5]

OUTPUT

[1, 2, 3, 5, 34, 56]


INPUT

arr = [1, 2, 4, 3, 56]
brr = [3, 5]

OUTPUT

Error : The input lists should be sorted.
"""

