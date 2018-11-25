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
1.  |------------|
2.  |---|
3.      |----|
4.      |------|
5.          |-----|
6.           |----|
In the above example, if we select task 1, no other task is compatible with it,
so we will get only one task completed and our profit will only be 1.
So we select 2 and now 1 is removed as it is not compatible; if we select 4 or \
5 now, 3 and 6 will be removed in either case because of compatibility issue \
and our profit will remain 2; so we select 3 and 6 to maximize our profit to 3 \
completable tasks.
This algorithm is called EARLIEST FINISH TIME INTERVAL SCHEDULING ALGORITHM.
'''

 
def initialize_task_set() :
    n = int(input(("Enter number of tasks:"))
            print(n)

def incompatible_task_remover() :
    pass

def schedular() :
    pass

def display_output() :
    pass

T = []    #A list of tasks
initialize_task_set()
