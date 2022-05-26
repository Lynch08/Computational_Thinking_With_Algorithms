# Selection sort in Python

# Generate numbers
#Import Random Module
import random

# Empty array
randomlist = [] 

# set len of array (10 elements - Zero indexing non inclusive)
for i in range(0,10): 
    #Range of values
    n = random.randint(1,300)
    #append to empty array
    randomlist.append(n)


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in ascending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


#data = [-2, 45, 0, 11, -9]
size = len(randomlist)
print('Pre_Sort: ', randomlist)
selectionSort(randomlist, size)
print('Post_Sort: ',randomlist)