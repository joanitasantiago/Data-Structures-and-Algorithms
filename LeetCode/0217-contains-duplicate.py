# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


def contains_duplicate(nums):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_improved(nums):
    
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def shorter_contains_duplicate(nums):

    return len(nums) != len(set(nums))

# set(nums) elimina duplicatas automaticamente pq um set é uma coleção de elementos únicos.

# se o tamanho de nums for diferente de set(nums) é pq tem duplicatas

# isso funciona pq o objetivo do problema é apenas saber se há ou não elementos duplicados com output de true ou false.



teste =  [1,2,2,3,4]

print(shorter_contains_duplicate(teste))