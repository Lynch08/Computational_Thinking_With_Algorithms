# Python3 implementation of QuickSort 
# Code adapted from https://www.geeksforgeeks.org/quick-sort/

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
 
# Function to find the partition position
def partition(array, low, high):
 
  # Choose the rightmost element as pivot
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
 
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
 
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  # Return the position from where partition is done
  return i + 1
 
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
 
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
 
    # Recursive call on the left of pivot
    quick_sort(array, low, pi - 1)
 
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)
 
   
         
# Driver code
print('Unsorted Array: ', randomlist) 
quick_sort(randomlist , 0, len(randomlist) - 1)
 
print('Sorted array: ', randomlist)