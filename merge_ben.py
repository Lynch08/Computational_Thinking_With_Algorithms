# the benchmarking algoirithms is based on the lecture materials, with modifications and additional comments
#  external Python libraries for building and analysing the dataset.

import numpy as np # numerical calculations
import pandas as pd # data manipulation
import time
################################# MERGE SORT #################################
##### Credits #####
# Source: https://stackabuse.com/sorting-algorithms-in-python/
# Adapted and commented by the author of this Notebook


# Auxiliary function, merging and sorting two arrays
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        
        if left_list_index < left_list_length and right_list_index < right_list_length:
            
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
                
            # If the item at the beginning of the right list is smaller, add it to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the element from the right list
        elif left_list_index == left_list_length:
            
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
            
        # If we've reached the end of the of the right list, add the elements from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    # final result of the sorting
    return sorted_list
    #print(sorted_list)
    
    
# Function performing the merge sort; it takes an array to be sorted as an argument
def merge_sort(array):
    
    # If the list is a single element, return it
    if len(array) <= 1:
        return array

    # Use floor division to get midpoint, indices must be integers
    mid = len(array) // 2

    # Sort and merge each half
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)
################################################### BENCHMARK ###################################################    
    

# creation of empty data (just headings)
data = pd.DataFrame(columns = ["Size", "Bubble", "Merge",  "Bucket", "Selection", "Quick", "Python"]) 

# adding values of the size column to the dataset, assumed arbitrarily, based on the project brief.
data["Size"] = (100, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000)

# generating arrays of random numbers, based on algorithm provided in the project brief
def random_array(size): 
    
    # create an empty array
    array = []
    
    # populate the arr list with randomly generated numbers
    for i in range(size):
        array.append(np.random.randint(0, 100)) # random integer numbers in range from 0 to 99
        
    return array

# populating the arrays for each test sizes
# create an empty container to hold the set of arrays
random_number_arrays = []

# loop through array sizes and for each one assign rundom numbers for each array size (array size is shown in "data" DataFrame, column "size")
for array_size in data["Size"]:
    
    # create an auxiliary counter representing the index 
    random_number_arrays_index = 0
    
    # call function random_array(), passing as an argument the number of elements to be generated
    random_number_arrays.append(random_array(array_size))
    
    # increment the counter by 1
    random_number_arrays_index += 1
    
#######################################
#   Merge Sort Benachmark                      
#######################################

# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 100, 250, 500, etc
for current_array in range(len(data["Size"])): 
    
    # a placeholder to store results for each test
    intermediate_results = []

    # perform the same sorting test several times in order to get the avarage time
    num_runs = 10 # number of the tests 
    
        
    # benchmarking algorithm 
    for r in range(num_runs):
        
        # make a copy of the array to preserve the original unsorted order for the remaining runs
        ar = random_number_arrays[current_array].copy() 
        
        # log the start time (time stamp)
        start_time = time.time()
    
           
        ##### call the sorting implementation to be benchmarked #####
        merge_sort(ar)
              
   
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
        
        # for each sorting instance, add the time to the below array
        intermediate_results.append(time_elapsed)
        #print(intermediate_results)
    # Average result from all runs for the current array size
    average_result = np.mean(intermediate_results) * 1000 # in milliseconds
    #print (average_result)
     
    #add the average time to the dataframe
    data.loc[current_array, "Merge"] = average_result
    
# Apply formating to three decimal places
# Source: https://stackoverflow.com/a/42735712
pd.options.display.float_format = '{:,.5f}'.format

# transpose the table, source: https://stackoverflow.com/a/31328974
d = data.transpose().reset_index().rename(columns={'index':'Size'})
new_header = d.iloc[0] #grab the first row for the header
d = d[1:] #take the data less the header row
d.columns = new_header #set the header row as the df header

# show the results in a table format
print(d)
