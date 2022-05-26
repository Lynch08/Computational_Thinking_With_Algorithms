# the benchmarking algoirithms is based on the lecture materials, with modifications and additional comments
#  external Python libraries for building and analysing the dataset.

import numpy as np # numerical calculations
import pandas as pd # data manipulation
import time
################################# BUCKET SORT#################################

# Insertion sort function to sort values once they have been divided into the buckets 
def insertion(inpvalue):
    # iterate through 1 at a time the length of the input value
    for i in range(1, len(inpvalue)):
        temp = inpvalue[i]
        # Move elements of arr[0..i-1], that are greater than temp, to one position ahead
        # of their current position
        j = i - 1
        while (j >= 0 and temp < inpvalue[j]):
            inpvalue[j + 1] = inpvalue[j]
            j = j - 1
        inpvalue[j + 1] = temp
        

#Function to Divide array in to buckets and then call insertion function within the fuction to sort the data in the buckets
def bucket_sort(inpvalue):
    # find largest value
    largest = max(inpvalue)
    # get number of items in array
    length = len(inpvalue)
    size = largest/length
    
    # set number of buckets
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(inpvalue[i]/size)
        # sort values into buckets
        if j != length:
            buckets[j].append(inpvalue[i])
        else:
            buckets[length - 1].append(inpvalue[i])
    # call insertion sort to sort values in buckets
    for i in range(length):
        insertion(buckets[i])
 
    res = []
    
    # Combine buckets to return sorted array 
    for i in range(length):
        res = res + buckets[i]
 
    return res

################################################### BENCHMARK ###################################################    
    

# creation of empty data (just headings)
data = pd.DataFrame(columns = ["Size", "Bubble", "Merge",  "Bucket", "Selection", "Quick", "Python"]) 

# adding values of the size column to the dataset
data["Size"] = (100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000)

# generating arrays of random numbers
def random_array(size): 
    
    # create an empty array
    array = []
    
    # populate the arr list with randomly generated numbers
    for i in range(size):
        # random integer numbers in range from 0 to 99
        array.append(np.random.randint(0, 100)) 
        
    return array

# populating the arrays for each test sizes
# create an empty container to hold the set of arrays
random_number_arrays = []

# loop through array sizes and for each one assign the relevent amount of random integers for each array size 
for arr_size in data["Size"]:
    
    # create a counter representing the index 
    random_number_arrays_index = 0
    
    # call function random_array(), passing as an argument the number of elements to be generated
    random_number_arrays.append(random_array(arr_size))
    
    # increment the counter by 1
    random_number_arrays_index += 1
    
    
#######################################
#   Bucket Sort Benachmark                      
#######################################

# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 100, 250, 500, etc
for current_array in range(len(data["Size"])): # Note: the last three arrays  tested for this sorting algorithm
        
    # a placeholder to store results for each test
    single_run_results = []

    # perform the same sorting test numerous times in order to calculate the avarage time
    num_runs = 10 # number of the tests 
    
    
    # benchmarking algorithm 
    for r in range(num_runs):
        
        # make a copy of the array to preserve the original unsorted order for the remaining runs
        ar = random_number_arrays[current_array].copy() 
        
        # log the start time (time stamp)
        start_time = time.time()
    
    
        ##### call the sorting implementation to be benchmarked #####
        bucket_sort(ar)
        #time.sleep(.5)
        
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
            
        # for testing - show time of each run
        #print("Time of run", r+1,":", time_elapsed, "\n")
    
        # for each sorting instance, add the time to the below array
        single_run_results.append(time_elapsed) 
    
    # Average result from all runs for the current array size
    average_result = np.mean(single_run_results) * 1000 # in milliseconds
    
    #add the average time to the dataframe
    data.loc[current_array, "Bucket"] = average_result
    
    
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
