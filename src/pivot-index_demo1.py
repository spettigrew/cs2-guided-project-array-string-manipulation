"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def old_pivot_index(nums):  #runtime O(n^2) (o of n squared)
    # Your code here
# U - input =  array of ints. Return a number (an index) if found. Return -1 otherwise

# Plan - search through array to find pivot index. Is i a pivot index? If true: return the index(i). If false: return
# Is index 2 a pivot index? Get sum of left subarray get sum of right subarray and compare.

    # search through nums list for a pivot index
    # go through each item in nums
    for i in range(len(nums)):
        # check if current index (i) is the pivot index. (slicing is exclusive)
        left_subarray = nums[:i]
        right_subarray = nums[i+1:] # nums[start(inclusive):end(exclusive)] 
        # get sum of left subarray 
        left_sum = sum(left_subarray)
        # get sum of right subarray
        right_sum = sum(right_subarray)
        # print(left_subarray, right_subarray)
        # check if they are equal
        if left_sum == right_sum:
            # if equal, return i
            return i
    #return -1
    return -1
    

def pivot_index_left_right(nums):
    # create Left sum and Right sum 
    l_sum = 0
    r_sum = sum(nums[1:])

    # search through the array and check if index is pivot index
    for i in range(len(nums)):
        # check if l_sum == r_sum
        if l_sum == r_sum:
            return i
        # add number at current index to left sum
        l_sum += nums[i]
        # check that we are not at the last index
        if (i+1 == len(nums)):
            r_sum = 0
        else:
            r_sum -= nums[i+1]
    return -1 

def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0

    # as we go through the array, update left_sum
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i] 
        if left_sum == right_sum:
            return i
        left_sum += nums[i]

    return -1


print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([]))