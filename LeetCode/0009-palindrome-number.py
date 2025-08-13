# Given an integer x, return true if x is a palindrome, and false otherwise.



# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

input = 5444445


def is_palindrome(x):

    number = str(x)

    reversed_number = ""

    for i in range(len(number) - 1, -1, -1):
        reversed_number += number[i]

    for n1, n2 in zip(number, reversed_number):
        if n1 != n2:
            return False
    
    return True

def improved_is_palindrome(x):
     
     number = str(x)

     return number == number[::-1]

print(is_palindrome(input))

print(improved_is_palindrome(input))


#### ver solução sem converter pra string