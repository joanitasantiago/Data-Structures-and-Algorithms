# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

def move_zeroes(nums):

    positition = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[positition], nums[i] = nums[i], nums[positition]
            positition += 1
    return nums

teste = [0,1,0,3,12,6,1,0,5,3,450,456456,0,48989,5456,1,25,5,6,8,0,0,0,0,5,10,9,11,12,7,0,0,5,0]

print(move_zeroes(teste))


