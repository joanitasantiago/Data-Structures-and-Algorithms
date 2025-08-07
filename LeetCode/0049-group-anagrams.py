# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

teste = ["eat","tea","tan","ate","nat","bat"]

def group_anagrams(input):

# ordena a string -> transforma em tupla pra poder usar como key do dicionário
# dicionários não deixam repetir chave, então toda string com os mesmos caracteres
# (mesmo bagunçados) vai cair na mesma key
# aí usa a string original como valor e junta tudo numa listinha

    anagrams_dict = dict()

    for item in input:
        key = tuple(sorted(item)) #pega os valores e transforma numa tupla. Pra ser key precisa ser imutável e o sorted retorna uma lista que é mutável. tuple é imutável, serve como key

        if key not in anagrams_dict:
            anagrams_dict[key] = [] #se n tiver a key ainda, cria e inicia a lista de valores

        anagrams_dict[key].append(item) #aponta pra key e acrescenta o item na lista de valores
    
    return list(anagrams_dict.values()) #retorna uma lista apenas com os valores do dicionário

#Tem uma solução mais eficiente:

# objetivo: pra cada palavra:
# 1.criar uma tupla de contagem de letras
# 2.usar como chave em um dicionário
# 3.adicionar a palavra no grupo daquela chave
# 4.retornar todos os grupos
# ver dps..

from collections import defaultdict

def group_anagrams2(input):
    anagrams_dict = defaultdict(list)

    for word in input:
        count = [0] * 26  # uma posição pra cada letra de a-z

        for letter in word:
            count[ord(letter) - ord('a')] += 1  # transforma letra em índice

        key = tuple(count)  # tupla imutável = chave válida

        anagrams_dict[key].append(word)  # agrupa os anagramas

    return list(anagrams_dict.values())

print(group_anagrams2(teste))