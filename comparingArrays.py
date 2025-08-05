# Given 2 arrays, creat a function that let's a user 
# know (true/false) wheter these two arrays
# contain any common items. For example:
# const array1 = [ 'a'. 'b', 'c', 'x'];
# const array2 = [ 'z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];
# const array2 = ['z'. 'y', 'x'];
# should return true.
# 2 parameters
# return true or false


array1 = ['a', 'b', 'c', 'd']

array2 = ['canela', 'y', 'c', 'i', '9']

# FORÇA BRUTA O(n^2)

def has_common_items(array1, array2):

    for item1 in array1:
        for item2 in array2:
           if item1 == item2:
               return True
           
    return False

# usdando conjuntos fica melhor O(n)

def has_common_items2(array1, array2):

    items = set(array1) #esse set() é um construtor, tb é uma forma de criar conjuntos

    for item in array2:
        if item in items:
            return True
    
    return False

print(has_common_items2(array1, array2))