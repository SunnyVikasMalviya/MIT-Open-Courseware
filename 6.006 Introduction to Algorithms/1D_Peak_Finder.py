'''
LOCAL PEAK(s) FINDER
The program finds and returns indices of all the local maximas from a given set\
of numbers. An index is a peak if the value at that index is greater than the\
values(value for the extreme indices) at the adjacent indices.
i.e.
for index i to be a peak a[i-1] <= a[i] <= a[i+1]

For finding the first local peak it encounters, just activate all the break \
statements.

Now, there can be two cases:
CASE 1: Peak always exist i.e. flat surfaces are considered peaks if they are\
        higher than surfaces adjacent to them.
        Diagramatically :

        _____________________       Is also a peak, considering a virtual valley
                                    adjacent to it.

                     _
         ___  ____  / \                        __
        /   \/    \/   \       3 Peaks Exists,/  \ are also considered as peaks.
      
      
CASE 2: Peak may not exist i.e. flat surfaces are not considered peaks even \
        if they are higher than surfaces adjacent to them.
        Diagramatically :

                    _
         ________  / \
        /        \/   \       No Peak Exists, only  /\ are considered as peaks.
        
        
'''


def initialize_elements() :
    list_ = list(int(x.strip()) for x in input("Enter elements for \
1D Peak finding:").split(' '))
    print(list_)
    peak_finder(list_)
    
def peak_finder(list_) :
    print("Indices with local maxima or peak are :")
    #print(list_)
    for i in range(len(list_)) :
        if i == 0 :
            if list_[i] >= list_[i+1] :      #CASE 1
            #if list_[i] > list_[i+1] :      #CASE 2
                display_output(i)
                #break
        elif i == len(list_)-1 :
            if list_[i] >= list_[i-1] :      #CASE 1
            #if list_[i] > list_[i-1] :      #CASE 2
                display_output(i)
                #break
        else :
            if list_[i] >= list_[i+1] and list_[i] >= list_[i-1] :     #CASE 1
            #if list_[i] > list_[i+1] and list_[i] > list_[i-1] :      #CASE 2
                display_output(i)
                #break

def display_output(i) :
    print(str(i))

initialize_elements()
