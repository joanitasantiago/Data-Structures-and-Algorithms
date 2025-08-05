#We are given an array of integers and a particular sum.
#We have to check if there are any two elements in the array that add up to the given sum.
#For example, array = [1,2,4,5] ,sum = 6
#This should return True as 2+4 = 6


# worst solution (nested loops)

def has_pair_sum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return True
    return False

print(has_pair_sum([1, 2, 4, 5], 6))       # True (2 + 4)
print(has_pair_sum([3, 1, 7, 9], 10))      # True (3 + 7)


# better solution
# nesse caso usei dicionário porém como só precisamos
# checar se o conteúdo existe ou não
# poderia ter usado set

def has_pair_sum2(array, target):

    items = dict()

    for i in range(len(array)):
        result = target - array[i]
        if result in items:
            return True
        else:
            items[array[i]] = i
    return False

print(has_pair_sum2([1, 2, 4, 5], 6))       # True (2 + 4)
print(has_pair_sum2([-2, 8, 15, -5], 13))   # True (-2 + 15)

# usando set pois não precisamos do índice, só precisamos verificar se o conteúdo existe ou não.

def has_pair_sum3(array, target):
    seen = set()

    for num in array:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False