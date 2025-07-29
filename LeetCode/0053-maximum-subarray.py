# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

def brute_force_max_subrarray_sum(nums):
    
    max_subarray_sum = float('-inf') #pegar o menor numero possivel

    for i in range(len(nums)):
        temp_sum = 0
        for j in range(i, len(nums)): 
            temp_sum += nums[j]
            if temp_sum > max_subarray_sum:
                max_subarray_sum = temp_sum

    return max_subarray_sum

def improved_max_subarray_sum(nums):

    max_subarray_sum = float('-inf')
    temp_sum = 0

    for num in nums:
        temp_sum += num
        if temp_sum > max_subarray_sum:
            max_subarray_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    
    return max_subarray_sum

# Kadane's algorithm is a greedy/dynamic programming algorithm that 
# can be used on an array. It is used to calculate the maximum sum 
# subarray ending at a particular position and typically runs in O(n) time.

teste1 = [1, 2, 3]                      # soma máxima: 6
teste2 = [-1, -2, -3]                   # soma máxima: -1
teste3 = [5]                            # soma máxima: 5
teste4 = [0, 0, 0]                      # soma máxima: 0
teste5 = [1, -2, 3, 4, -1, 2]           # soma máxima: 8
teste6 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # soma máxima: 6
teste7 = [-2, -3, 4, -1, -2, 1, 5, -3]    # soma máxima: 7
teste8 = [-10, 100, -200, 300]         # soma máxima: 300
teste9 = [100, -1, -1, -1, -1]         # soma máxima: 100
teste10 = [-5, -1, -8, -9]             # soma máxima: -1
teste11 = [0, -3, 5, -2, 0, 4]         # soma máxima: 7
teste12 = [-2, 0, -1, 0, -3]           # soma máxima: 0

print(brute_force_max_subrarray_sum(teste8))
print(brute_force_max_subrarray_sum(teste2))
print(brute_force_max_subrarray_sum(teste3))

print("-------")

print(improved_max_subarray_sum(teste8))
print(improved_max_subarray_sum(teste2))
print(improved_max_subarray_sum(teste3))