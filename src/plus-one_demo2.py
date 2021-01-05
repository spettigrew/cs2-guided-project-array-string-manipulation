"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""

# for loop = strict progression from cause to effect
# while loop = a non-linear, non-subjective viewpoint
def plus_one(digits):
    # Your code here
    # U - input -  array (not empty). Output -  array
        # length never greater than 100 and i will not be greater than 9
        # Plan - add 1 to each index going backwards to front.
        # create a 'carry' if the num is 9 (9+1 =10)
        # add 1 to the current carried digit 
    digit_index = len(digits) - 1

    while digit_index >= 0:
        # add one to digits
        digits[digit_index] += 1
            # check if this digit overflows (to 10)
        if digits[digit_index] < 10:
            return digits
        else:
            # this value is too large, set it to 0
            # continue the loop
            digits[digit_index] = 0
            digit_index -= 1
    # If we get here, that means that we had all 9's and we still need to add 1
    return [1] + digits      
            

        