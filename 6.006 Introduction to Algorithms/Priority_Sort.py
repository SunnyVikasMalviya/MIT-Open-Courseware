import pandas as pd
from Counting_Sort import counting_sort


def priority_sort(path) :
    """
    File sort takes a csv file and sorts it on the basis of all of its columns
    based on the priority of columns(considering columns occurring at the right
    are of lower priority than the left ones).
    priority_sort()
    1. reads the input from a csv file
    2. converts it into a dataframe using pandas
    3. one by one sends columns(in order of ascending priority) to
    counting_sort() which returns a sorted list.
    4. arranges the whole file using the returned list.
    5. creates a new csv file and stores it in the same place as the original
    with the same name appended with '1'.
    6. returns the path of the new file
    Arguments
    1. path : path of the csv file that has the data
    Returns
    1. res_path : path of the csv file that has the sorted data
    """
    #OPENING CSV FILE
    df = pd.read_csv(path)
    #GETTING THE COLUMNS
    col = df.columns
    #TRANSPOSE OF THE DATAFRAME
    dft = df.transpose()
    #COLUMNS THAT WILL BE USED IN SORTING
    col_for_sort = col[1:]
    i = len(col_for_sort)
    j = len(dft.columns)
    k = 0
    #ACTUALLY SORTING USING counting_sort()
    for c in reversed(col_for_sort) :
        sorted_c = counting_sort(list(df[c]))
        for val in sorted_c :
            for x in range(j-k) :
                if dft[x][i] == val :
                    k += 1
                    temp = dft.pop(x)
                    dft[x] = temp
                    print(dft)
                    break
        i -= 1
        k = 0
    res_path = path[:-4] + '_1.csv'
    dft.transpose().to_csv(res_path)
    return res_path

if __name__ == '__main__' :
    file_path = 'C:\MvikBack\Python\ToUpload\MIT 6.006\ex.csv'
    #Now considereing the left most columns have the most significant
    #data or the data with the higher priority and the right most
    #columns have the least significant data or data with lesser priority.
    new_path = priority_sort(file_path)
    print(new_path)
    

"""
INPUT

File Path : C:\MvikBack\Python\ToUpload\MIT 6.006\Eg_Priority_Sort.csv

  Student  Class 5  Class 4  Class 3  Class 2  Class 1
0       A        8        6        1        2        3
1       B        4        6        7        3        7
2       C        0        5        1        2        5
3       D        1        6        4        1        3
4       E        8        4        1        0        2
5       F        1        3        3        1        9
6       G        6        1        3        6        0
7       H        8        3        5        9        5
8       I        8        0        4        4        4
9       J        1        0        8        7        8

OUTPUT

File Path : C:\MvikBack\Python\ToUpload\MIT 6.006\Eg_Priority_Sort_1.csv
"""
