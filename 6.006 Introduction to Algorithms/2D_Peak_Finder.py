'''
LOCAL 2D PEAK(s) FINDER
The program finds and returns index of a local maxima from a given matrix\
of numbers. An index is a peak if the value at that index is greater than the\
values at the adjacent indices.
'''
def initialize_elements() :
    n = int(input("Enter number of rows in the matrix:"))
    matrix = [[0 for x in range(1)] for y in range(n)]
    #print(matrix)
    for i in range(n) :
        lst = list(int(x.strip()) for x in input().split(' '))
        matrix[i] = lst            
    print(matrix)
    print("Index with local maxima or peak is :")
    peak_2d = peak_finder(matrix)
    display_output(peak_2d)
    
def peak_finder(mat) :
    j = int(len(mat[0])/2)
    col_max = -1
    for x in range(len(mat)) :
        if col_max < mat[x][j] :
            col_max = mat[x][j]
            i = x
    if mat[i][j] < mat[i][j-1] and j-1 >= 0 :
        mat1 = [[0 for a in range(1)] for b in range(len(mat))]
        for p in range(mat) :
            for q in range[0:j+1] :
                mat1[p][q] = mat[i][j]
        peak = peak_finder(mat1)
    elif mat[i][j] < mat[i][j+1] and j+1 < len(mat[0]) :
        mat1 = [[0 for a in range(1)] for b in range(len(mat))]
        for p in range(mat) :
            for q in range[j:len(mat[0])] :
                mat1[p][q] = mat[i][j]

        mat1 = mat[0:len(mat), j:len(mat[0])]
        peak = peak_finder(mat1)
    else :
        peak = mat[i][j]
        return peak
    return peak
        
def display_output(peak_2d) :
    print(peak_2d)

initialize_elements()

'''
Note : Matrices don't exist in python implicitly. Hence, a line like A = [][] \
will produce an error. First, we have to intialize the outer lists before \
adding items to the inner list. It's called list comprehension in python. 
'''
