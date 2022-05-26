# Here is the file with all the sorting functions (and any auxzillary functions that they require to run), bench marking algorithms
# data generation (arrays with ints from 0-99 of different sizes).

# The Benchmarking algoirithms is based on the lecture materials, with modifications where required for 
# the inputs of the sorting functions.

# 


# External Python libraries for building and analysing the dataset.
import numpy as np # numerical calculations
import pandas as pd # data manipulation
import time
import matplotlib.pyplot as plt

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
                
################################# MERGE SORT #################################

# Create merge sort function
# Source: https://stackabuse.com/sorting-algorithms-in-python/


# Auxiliary function, merging and sorting two arrays
def merge(sub_l, sub_r):
    sorted_list = []
    sub_l_index = sub_r_index = 0

    # make the list lengths variables
    sub_l_len, sub_r_len = len(sub_l), len(sub_r)

    for _ in range(sub_l_len + sub_r_len):
        
        if sub_l_index < sub_l_len and sub_r_index < sub_r_len:
            
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if sub_l[sub_l_index] <= sub_r[sub_r_index]:
                sorted_list.append(sub_l[sub_l_index])
                sub_l_index += 1
                
            # If the item at the beginning of the sub_r list is smaller, add it to the sorted list
            else:
                sorted_list.append(sub_r[sub_r_index])
                sub_r_index += 1

        # If we've reached the end of the of the sub_l list, add the element from the sub_r list
        elif sub_l_index == sub_l_len:
            
            sorted_list.append(sub_r[sub_r_index])
            sub_r_index += 1
            
        # If we've reached the end of the of the right list, add the elements from the left list
        elif sub_r_index == sub_r_len:
            sorted_list.append(sub_l[sub_l_index])
            sub_l_index += 1

    # final result of the sorting
    return sorted_list

# Function performing the merge sort; it takes an array to be sorted as an argument
def merge_sort(array):
    
    # If the list is a single element, return it
    if len(array) <= 1:
        return array

    # Use floor division to get midpoint, indices must be integers
    mid = len(array) // 2

    # Sort and merge each half
    sub_l = merge_sort(array[:mid])
    sub_r = merge_sort(array[mid:])

    # Merge the sorted lists into a new one
    return merge(sub_l, sub_r)
        
################################# BUCKET SORT#################################

# Create merge bucket sort function
# Source: https://www.programiz.com/dsa/bucket-sort and https://www.geeksforgeeks.org/bucket-sort-2/


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


# Function to Divide array in to buckets
# Then call insertion function within the fuction to sort the data in the buckets
def bucket_sort(inpvalue):
    # find largest value
    largest = max(inpvalue)
    # return number of items in array
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
    
    # empty array to store results
    res = []
    
    # Combine buckets to return sorted array 
    for i in range(length):
        res = res + buckets[i]
 
    return res



################################# SELECTION SORT#################################

# Create merge sort function
# Source: https://www.programiz.com/dsa/selection-sort

def selectionSort(array, size):
   
   # iterate through each element
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in ascending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put elements in the correct positions
        (array[step], array[min_idx]) = (array[min_idx], array[step])


################################# QUICK SORT#################################

# Create quick sort function
# Source: https://www.geeksforgeeks.org/quick-sort/

# Function to find the partition position
def partition(array, low, high):
 
  # Choose the rightmost element as pivot
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Iterate through all elements
  # compare each element with pivot
  for j in range(low, high):
      # make item individual array
    if array[j] <= pivot:
      # If element less than, than pivot is found
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


################################################### BENCHMARK ###################################################    
    
########Creation of Data########

# creation of empty data (just headings)
data = pd.DataFrame(columns = ["Input Size", "Bubble", "Merge",  "Bucket", "Selection", "Quick"]) 
data_merg = pd.DataFrame(columns = ["Input Size", "Bubble", "Merge",  "Bucket", "Selection", "Quick"])
# adding values of the size column to the dataset, assumed arbitrarily, based on the project brief.
data["Input Size"] = (200, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000)#(100, 250, 500, 750, 1000), 


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

# loop through array sizes and for each one assign random numbers for each array size (array size is shown in "data" DataFrame, column "size")
for array_size in data["Input Size"]:
    
    # create an auxiliary counter representing the index 
    random_number_arrays_index = 0
    
    # call function random_array(), passing as an argument the number of elements to be generated
    random_number_arrays.append(random_array(array_size))
    
    # increment the counter by 1
    random_number_arrays_index += 1


#######################################Bubble Sort Benachmark#######################################               


# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 200, 1250, 2500,...
for current_array in range(len(data["Input Size"])): 
    
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

#######################################Merge Sort Benachmark#######################################               


# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 200, 1250, 2500,...
for current_array in range(len(data["Input Size"])): 
    
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
    
        sub_r = []   
        ##### call the sorting implementation to be benchmarked #####
        merge_sort(ar)
              
   
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
        
        # for each sorting instance, add the time to the below array
        temp_results.append(time_elapsed)
    
    # Average result from all runs for the current array size
    average_result = np.mean(temp_results) * 1000 # in milliseconds
     
    #add the average time to the dataframe
    data.loc[current_array, "Merge"] = average_result
    
    
#######################################Bucket Sort Benachmark#######################################            


# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 200, 1250, 2500,...
for current_array in range(len(data["Input Size"])):
        
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
        bucket_sort(ar)
        
        
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
            
        # for testing - show time of each run
        #print("Time of run", r+1,":", time_elapsed, "\n")
    
        # for each sorting instance, add the time to the below array
        temp_results.append(time_elapsed) 
    
    # Average result from all runs for the current array size
    average_result = np.mean(temp_results) * 1000 # in milliseconds
    
    #add the average time to the dataframe
    data.loc[current_array, "Bucket"] = average_result
    
#######################################SelectionSort Benchmark#######################################          


# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 200, 1250, 2500,...
for current_array in range(len(data["Input Size"])): 
    
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
        selectionSort(ar, len(ar))
        
        
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
         
        # for each sorting instance, add the time to the below array
        temp_results.append(time_elapsed)
    
    # Average result from all runs for the current array size
    average_result = np.mean(temp_results) * 1000 # in milliseconds
    
    #add the average time to the dataframe
    data.loc[current_array, "Selection"] = average_result
    
####################################### Quicksort Benchmark #######################################

# loop through each array size defined in the data["Size"] column, that is arrays of quantity of elements 200, 1250, 2500,...
for current_array in range(len(data["Input Size"])): 
    
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
        quick_sort(ar, 0, len(ar) - 1)
        
        
        # log the end time (time stamp)
        end_time = time.time()
        
        # calculate the elapsed time
        time_elapsed = end_time - start_time
         
        # for each sorting instance, add the time to the below array
        temp_results.append(time_elapsed)
    
    # Average result from all runs for the current array size
    average_result = np.mean(temp_results) * 1000 # in milliseconds
    
    #add the average time to the dataframe
    data.loc[current_array, "Quick"] = average_result

    
####################################### FORMATING DATA #######################################  
    
# Apply formating to three decimal places
# Source: https://stackoverflow.com/a/42735712
pd.options.display.float_format = '{:,.3f}'.format

# transpose the table, source: https://stackoverflow.com/a/31328974
ben_df = data.transpose().reset_index().rename(columns={'index':'Input Size'})

#first row is header
new_header = ben_df.iloc[0] 

#data without header row
ben_df = ben_df[1:] 

# row is dataframe headers
ben_df.columns = new_header 

# show the results in a table format
print(ben_df)

ben_df.to_excel("output.xlsx", sheet_name='Benchmark_data', index=False)

####################################### PLOTTING THE DATA ####################################### 

# Setting up the plotting output
plt.plot(data['Input Size'], data['Bubble'], label='Bubble_Sort O(n²)', linewidth=4)
plt.plot(data['Input Size'], data['Quick'],  label='Quick_sort O(n log(n))', linewidth=4)
plt.plot(data['Input Size'], data['Bucket'], label='Bucket_Sort O(n + k)', linewidth=4)
plt.plot(data['Input Size'], data['Merge'],  label='Merge_Sort O(n log(n))', linewidth=4)
plt.plot(data['Input Size'], data['Selection'], label='Selection_Sort O(n²)', linewidth=4)



# Adding title, labels and legend
plt.title("Measured Time Complexity", fontsize=20)
plt.xlabel("Input Size", fontsize=18) 
plt.ylabel("Time (Milliseconds)" ,fontsize=18)
plt.legend()
plt.legend(fontsize=14)

# set axis ranges
plt.xlim(0,10000)
plt.ylim(0,3000)

# set size of the plot in inches (dpi=100)
plt.gcf().set_size_inches(12, 6)

# save the graph
plt.savefig('Benchmark_Sort_Times.png')

# plot the graph
plt.show()

