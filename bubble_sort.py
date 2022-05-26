# Function performing the bubble sort; it takes an array if random numbers to be sorted as an argument


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



# Create bubble sort function
# Code adapted from https://stackabuse.com/bubble-sort-in-python/

def bubble_sort(array):
    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        # loop through each element of the array
        for i in range(len(array) - 1):
            #compare to element on the right
            if array[i] > array[i+1]:
                # Swap
                array[i], array[i+1] = array[i+1], array[i]
                has_swapped = True
                
    

#Array Before Sort    
print("Pre_Sort:",randomlist)

#Call The Function
bubble_sort(randomlist)

#Array After Sort
print("Post_Sort",randomlist)