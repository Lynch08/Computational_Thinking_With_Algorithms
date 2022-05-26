# Bucket Sort in Python
# Code adapted from https://cppsecrets.com/users/17211410511511610510710997106117109100971144964103109971051084699111109/Python-program-for-bucket-sort-algorithm.php
# And Code adapted from https://www.geeksforgeeks.org/bucket-sort-2/?ref=gcse
# For benchmarking
import time

# insertion_sort algorithm
def insertion(inpvalue):
    # Traverse through 1 to len(arr)
    for i in range(1, len(inpvalue)):
        temp = inpvalue[i]
        # Move elements of arr[0..i-1], that are greater than temp, to one position ahead
        # of their current position
        j = i - 1
        while (j >= 0 and temp < inpvalue[j]):
            inpvalue[j + 1] = inpvalue[j]
            j = j - 1
        inpvalue[j + 1] = temp

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
    
    for i in range(length):
        res = res + buckets[i]
 
    return res
 


num_runs = 10
results  = []
for r in range (num_runs):
    inpvalue = input('Enter the list of (nonnegative) numbers, hit space bar between each entry and return to finish: ').split()
    inpvalue = [int(x) for x in inpvalue]
    
    start_time = time.time_ns()
    sorted_list = bucket_sort(inpvalue)
    end_time = time.time_ns()
    time_elapsed = end_time - start_time
    results.append(time_elapsed)

print('Sorted list: ', end='')
print(sorted_list)
print('Time taken: ', time_elapsed)
print('Results: ', results)