# the benchmarking algoirithms is based on the lecture materials, with modifications and additional comments
#  external Python libraries for building and analysing the dataset.
import numpy as np # numerical calculations
import pandas as pd # data manipulation
import time

################################# BUBBLE SORT #################################
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
                

# creation of empty data (just headings)
data = pd.DataFrame(columns = ["Size", "Bubble", "Merge",  "Bucket", "Selection", "Quick", "Python"]) 

# adding values of the size column to the dataset, assumed arbitrarily, based on the project brief.
data["Size"] = (100, 250, 500, 750, 1000)#, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000)

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


# Apply formating to three decimal places
# Source: https://stackoverflow.com/a/42735712
#######################################
#   Bubble Sort Benachmark                      
#######################################

# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 100, 250, 500, etc
for current_array in range(len(data["Size"])): 
    
    # a placeholder to store results for each test
    temp_results = []

    # perform the same sorting test several times in order to get the avarage time
    num_runs = 10 # number of the tests 
    
        
    # benchmarking algorithm 
    for r in range(num_runs):
        
        # make a copy of the array to preserve the original unsorted order for the remaining runs
        ar = random_number_arrays[current_array].copy() 

        # log the start time (time stamp)
        start_time = time.time()
        
        
        ##### call the sorting implementation to be benchmarked #####
        bubble_sort(ar)
        
           
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
        
        # for each sorting instance, add the time to the below array
        temp_results.append(time_elapsed)
    
    # Average result from all runs for the current array size
    average_result = np.mean(temp_results) * 1000 # in milliseconds
    
    
    #add the average time to the dataframe
    data.loc[current_array, "Bubble"] = average_result
    
####Results####

pd.options.display.float_format = '{:,.5f}'.format

# transpose the table, source: https://stackoverflow.com/a/31328974
d = data.transpose().reset_index().rename(columns={'index':'Size'})
new_header = d.iloc[0] #grab the first row for the header
d = d[1:] #take the data less the header row
d.columns = new_header #set the header row as the df header

# show the results in a table format
print(d)