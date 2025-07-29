# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.



#solução 1 - não é a mais eficiente

input = [2,7,11,15]
target = 9

class solution1:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1): #percorre do index 0 até o penúltimo
            for j in range(i+1, len(nums)): #percorre do index 1 até o último
                if nums[i] + nums[j] == target:
                    return([i, j])
            

class solution2:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexmap = {} #dicionário p armazenar os numeros já vistos e seus índices
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indexmap:
                return [indexmap[diff], i]
            indexmap[num] = i


sol1 = solution1() #precisa criar um objeto da classe antes de chamar o método
result1 = sol1.twoSum(input, target)

sol2 = solution2()
result2 = sol2.twoSum(input, target)

print(f"Resultado com a solução 1: ", result1)
print(f"resultado com a solução 2: ", result2)