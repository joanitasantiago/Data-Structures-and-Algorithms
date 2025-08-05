texto = "Esse é o meu texto"

def reverse_string(string):
    reversed_text = ""
    for char in string:
        reversed_text = char + reversed_text
    return reversed_text


def reverse_string_improved(string):
    return string[::-1]

# string[start:stop:step]
# start: índice de início (opcional)

# stop: índice de fim (opcional)

# step: passo (pode ser positivo ou negativo)

# string[::-1] significa:
# Comece do final (start ausente)

# Vá até o início (stop ausente)

# Com passo -1, ou seja, de trás pra frente


print(f"1: {reverse_string(texto)}")

print(f"2: {reverse_string_improved(texto)}")