# Given a string s, the task is to find the lexicographically smallest string that can be formed by removing at most one character from the given string. 

# Examples: 

# Input: s = "abcda"  
# Output: "abca"
# Explanation: One can remove 'd' to get "abca" which is 
# the lexicographically smallest string possible. 

# Input: s = "aaa"
# Output: "aa"


# STRING SLICING
# s[start:stop:step]
# start: onde começa (default: 0)

# stop: onde termina (default: até o fim) É EXCLUSIVO

# step: o intervalo de salto


string = "abcedapt"

def lex_smallest_string(S):

    for i in range(len(S) - 1): #pra q o indice ultrapasse o tamanho da string. Estamos comparando i com i+1
        if S[i] > S[i+1]:
            return S[:i] + S[i+1:]
    return S[:-1]


#outra forma de fazer porém menos eficiente :)

def terrible_lex_smallest_string(S):

    to_be_removed = -1
    newString = ""

    for i in range(len(S) - 1):
        if S[i] > S[i+1]:
            to_be_removed = i
            break

    if to_be_removed >= 0:
        for i in range(len(S)):
            if i != to_be_removed:
                newString = newString + S[i]
    else: 
        for i in range(len(S) - 1):
            newString = newString + S[i]
    
    return newString


# list.append() é O(1).

# newString = newString + x é O(n²) no pior caso, porque cria strings novas a cada passo.

# "".join(list) só percorre a lista uma vez no final e concatena tudo de forma otimizada.

def less_terrible_lex_smallest_string(S):
    to_be_removed = -1
    new_chars = []

    for i in range(len(S) - 1):
        if S[i] > S[i + 1]:
            to_be_removed = i
            break

    if to_be_removed >= 0:
        for i in range(len(S)):
            if i != to_be_removed:
                new_chars.append(S[i]) #append() adds an element at the end of the list
    else:
        for i in range(len(S) - 1):
            new_chars.append(S[i])
    
    return "".join(new_chars) #The join() method takes all items in an iterable and joins them into one string.


