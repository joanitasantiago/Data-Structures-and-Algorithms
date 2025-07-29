# Em Python, embora não exista um tipo nativo chamado "array" usamos listas (list) como substituto
# As listas em Python são estruturas dinâmicas que permitem armazenar múltiplos valores de qualquer
# tipo, misturado ou não, com redimensionamento automático e métodos práticos como append(), remove() e sort(). 
# Já o módulo array, disponível através de from array import array, oferece uma estrutura mais próxima
# dos arrays tradicionais, mas com limitações: aceita apenas tipos homogêneos (como inteiros ou floats)
# e é usado principalmente quando se busca melhor desempenho em operações numéricas ou uso mais eficiente
# de memória. Assim, enquanto o array do módulo pode ser útil em cenários específicos, as listas são muito 
# mais versáteis e são a escolha padrão para armazenar coleções de dados em Python.

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position. Returns removed value.
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# quando usamos x = fruits, estamos apenas criando uma nova referência
# para o mesmo objeto na memória, ou seja, as duas variáveis apontam para a mesma 
# lista — qualquer modificação feita em uma refletirá na outra. Já ao usar 
# x = fruits.copy(), criamos uma cópia independente da lista original, 
# e as alterações feitas em fruits_list não afetam fruits, pois agora são objetos 
# distintos.

# diferença entre append() e extend() é que append() adiciona um único elemento à lista, 
# mesmo que esse elemento seja outra lista, enquanto extend() adiciona cada item de um iterável 
# (como outra lista) individualmente à lista original. Por exemplo, lista.append([2, 3]) adiciona 
# uma única sublista, resultando em [1, [2, 3]], enquanto lista.extend([2, 3]) adiciona os elementos 
# separadamente, resultando em [1, 2, 3].


texto = "Esse é o meu texto"

def reverse_String(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_String(texto))


print(texto.translate())