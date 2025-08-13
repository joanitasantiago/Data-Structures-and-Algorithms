# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


input = ["neet","code","love","you", "abobora", "otorrinolaringologista"]

class Solution:

    def encode(self, strs: list[str]) -> str:

        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word #cria uma string com o tamamho da palavra e um separador p poder usar de referência pra próxima função

        return encoded_string

    def decode(self, s: str) -> list[str]:

        i = 0
        decoded_string = []

        while i < len(s):
            j = i
            while s[j] != "#":      
                j += 1
            word_length = int(s[i:j]) #pega o tamanho da palavra q adicionamos lá em cima
            string_limit = j + 1 + word_length 

            decoded_string.append(s[j+1:string_limit])

            i = string_limit

        return decoded_string

sol = Solution()  #precisa criar um objeto da classe antes de chamar o método


print(f"Resultado: {sol.encode(input)}")
print(f"Resultado: {sol.decode(sol.encode(input))}")