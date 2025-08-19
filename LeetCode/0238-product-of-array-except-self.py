# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


input = [1,2,3,4]

def bf_product_of_array_except_self(nums):

    res = [0] * (len(nums))

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product = product * nums[j]
        res[i] = product

    return res

def improved_product_of_array_except_self(nums):

    res = [0] * len(nums) # cria um array de resultado do mesmo tamanho da entrada
    prefix_prod = 1 # guarda o produto acumulado da esquerda (começa em 1 pq é neutro da multiplicação)
    suffix_prod = 1 # guarda o produto acumulado da direita (também começa em 1)

    for i in range(len(nums)):
       res[i] = prefix_prod # salva no resultado o produto de todos os números à esquerda do índice
       prefix_prod *= nums[i]  # atualiza o produto acumulado multiplicando pelo número atual

    for i in range(len(nums) - 1, -1, -1): # percorre o array da direita pra esquerda
        res[i] *= suffix_prod # multiplica o valor salvo (prefixo) pelo produto da direita
        suffix_prod *= nums[i] # atualiza o produto acumulado multiplicando pelo número atual

    return res

#ler sobre prefix array/suffix array

print(improved_product_of_array_except_self(input))