# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

#Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



# s[i] precisa estar em t, independente da ordem

s = "anagram"
t = "nagaram"

def is_valid_anagram(s, t):

    aux_temp = ""
    first_string = list(s)
    second_string = list(t)

    #ver se tem o mesmo tamanho, se n tiver já retorna falso:
    if len(s) != len(t):
        return False
    else:
        # primeiro fazer um sorting nas strings
        for i in range(len(first_string) - 1):
            for j in range(i+1, len(first_string)):
                if first_string[i] > first_string[j]:
                    aux_temp = first_string[i]
                    first_string[i] = first_string[j]
                    first_string[j] = aux_temp
        
        for i in range(len(second_string) - 1):
            for j in range(i+1, len(second_string)):
                if second_string[i] > second_string[j]:
                    aux_temp = second_string[i]
                    second_string[i] = second_string[j]
                    second_string[j] = aux_temp

        # comparar
        for i in range(len(first_string)):
            if first_string[i] != second_string[i]:
                return False
        return True
    

#  Versão otimizida usando dicionário: chave = caracter, valor = x que aparece
#  Vamos verificar o tamanho logo no início e já retornar falso se n for igual
#  Contar a frequência dos caracteres e popular os dicionários
#  Comparar os dicionários -  Por que isso funciona?
#                             Porque o operador == em dicionários verifica se:
#                             1. Ambos têm as mesmas chaves
#                             2. Para cada chave, os valores são iguais
#                             3. a ordem interna das chaves não importa.
#  Essa solução atende ao follow up (compatível com qlquer caracter unicode)

def improved_is_valid_anagram(s, t):

    if len(s) != len(t):
        return False
    else:
        
        dict_s = dict()
        dict_t = dict()
        
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
                

        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        if dict_s == dict_t:
            return True
        else:
            return False

# No python tem uma ferramenta q pode usar pra simplificar isso tudo
# Ela segue a mesma lógica desse código - serve para contar quantas vezes cada elemento aparece em um iterável
# Counter é uma classe especial do módulo collections, que cria objetos 
# parecidos com dict, mas feitos para contar quantidades de forma automática e eficiente.
# Ficaria assim:

# from collections import Counter

# def is_anagram(s, t):
#     return Counter(s) == Counter(t)

print(improved_is_valid_anagram(s, t))
