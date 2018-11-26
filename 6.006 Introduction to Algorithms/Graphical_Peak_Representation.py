from matplotlib import pyplot as plt

def initialize_elements() :
    list_ = list(int(x.strip()) for x in input("Enter elements for \
1D Peak finding:").split(' '))
    print(list_)
    peak_finder(list_)
    return list_
    
def peak_finder(list_) :
    print("Indices with local maxima or peak are :")
    #print(list_)
    for i in range(len(list_)) :
        if i == 0 :
            if list_[i] >= list_[i+1] :      
            #if list_[i] > list_[i+1] :
                display_output(i, list_)
                #break
        elif i == len(list_)-1 :
            if list_[i] >= list_[i-1] :
            #if list_[i] > list_[i-1] :
                display_output(i, list_)
                #break
        else :
            if list_[i] >= list_[i+1] and list_[i] >= list_[i-1] :
            #if list_[i] > list_[i+1] and list_[i] > list_[i-1] :
                display_output(i, list_)
                #break

def display_output(i, list_) :
    print(str(i))
    lst.append((i, list_[i]))

lst = []
list_ = initialize_elements()
print('Peaks are the red points in the graph')
x = []
for y in range(len(list_)):
    x.append(y)
plt.plot(x, list_)
for i in lst :
    plt.scatter(i[0], i[1], color='r')
plt.show()


'''
Enter elements for 1D Peak finding:12 3 4 5 6 3 23 24 25 3 16
[12, 3, 4, 5, 6, 3, 23, 24, 25, 3, 16]
Indices with local maxima or peak are :
0
4
8
10

'''






