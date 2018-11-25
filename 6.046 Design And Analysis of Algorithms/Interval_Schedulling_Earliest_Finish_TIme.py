'''
INTERVAL SCHEDULING
Ques : Given a set of tuples, elements of which denote the start and finish \
time of tasks, write a program to select the maximum number of completeable \
tasks which are compatible with each other.
Compatible tasks : If s(j)>=f(i), tasks i and j are said to be compatible,
where s(j): starting time of jth task, f(i) : finish time of ith task.
The tasks are unweighted, meaning each task has equal profit, so we have to \
maximize the number of completeable tasks to maximize our profit.

eg:
Task    Time axis-->
    0 1 2 3 4 5 6 7 8 9
1.  |-------------|
2.  |---|
3.      |-----|
4.      |-------|
5.          |-----|
6.            |-----|
In the above example, if we select task 1, no other task is compatible with it,
so we will get only one task completed and our profit will only be 1.
So we select 2 and now 1 is removed as it is not compatible; if we select 4 or \
5 now, 3 and 6 will be removed in either case because of compatibility issue \
and our profit will remain 2; so we select 3 and 6 to maximize our profit to 3 \
completable tasks.
This algorithm is called EARLIEST FINISH TIME INTERVAL SCHEDULING ALGORITHM.
'''

def initialize_task_set() :
    n = int(input("Enter number of tasks:"))
    #print(n)
    for i in range(n):
        x = chr(i+65)
        print("For Task",str(x))
        #s = int(input())
        #f = int(input())
        #task_time = (s, f)
        task_time = tuple(int(y.strip()) for y in input().split(' '))
        if task_time[1] > task_time[0] :
            T[x] = task_time
    print(T)
    schedular()
    

def incompatible_task_remover(x) :
    for y in list(T) :
        if x != y :            
            if T[x][1] > T[y][0] :
                T.pop(y)

def eft_finder() :     #A function to find earlier finish time
    if len(list(T)) == 0 :
        return -1
    for x in list(T) :
        eft = T[x][1]     #eft : earliest finish time
        break
    for x in list(T) :
        if T[x][1] < eft :
            eft = T[x][1]
    return eft

def lft_finder() :    #A function to find last finish time
    if len(list(T)) == 0 :
        return -1
    for x in list(T) :
        lft = T[x][1]     #lft : last finish time
        break
    for x in list(T) :
        if T[x][1] > lft :
            lft = T[x][1]
    return lft
        
def schedular() :
    eft = eft_finder()
    lft = lft_finder()
    while eft <= lft :
        for x in list(T) :
            if T[x][1] == eft :
                incompatible_task_remover(x)
                T_completable[x] = T[x]
                T.pop(x)
                break
        eft = eft_finder()
        lft = lft_finder()
        if eft == -1 or lft == -1:
            break
    display_output()

def display_output() :
    print(T_completable)

T = {}    #A dictionary of tasks
T_completable = {}     #A dictionary of completable tasks
initialize_task_set()




'''
OUTPUT 1
Enter number of tasks:6
For Task A
0 7
For Task B
0 2
For Task C
2 5
For Task D
2 6
For Task E
4 7
For Task F
5 8
{'A': (0, 7), 'B': (0, 2), 'C': (2, 5), 'D': (2, 6), 'E': (4, 7), 'F': (5, 8)}
{'B': (0, 2), 'C': (2, 5), 'F': (5, 8)}
'''
'''
OUTPUT 2
Enter number of tasks:3
For Task A
3 6
For Task B
4 2
For Task C
0 4
{'A': (3, 6), 'C': (0, 4)}
{'C': (0, 4)}
'''
