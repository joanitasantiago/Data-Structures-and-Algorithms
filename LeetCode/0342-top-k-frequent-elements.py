# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


nums = [1,1,1,4,4,5,3,3]
k = 2

def top_k_frequent(nums, k):

    freq_map = dict()

    bucket = [[] for _ in range(len(nums) + 1)] # usamos _ por convenção qndo n queremos usar o valor de uma variável
                                                # range(len(nums) + 1 pra ter os índices de 0 a n (tamanho de nums))
                                                # ver list comprehension
    result = []

    for n in nums:
        if n in freq_map:
            freq_map[n] += 1
        else:
            freq_map[n] = 1

    for key, value in freq_map.items():
        bucket[value].append(key)

    for i in range(len(bucket) - 1, 0, -1): #começa do maior índice, stop no 0 (0 ta sempre vazio, n precisa dele), -1 é o 'passo' p andar de trás pra frente
        for number in bucket[i]:
            result.append(number)
            if len(result) == k:
                return result



print(top_k_frequent(nums, k))


