entrada = input("Ingresa los elementos separados por comas: ")

# Convertir la cadena a lista
lista = [x.strip() for x in entrada.split(",")]

tupla_resultado = tuple(set(lista))

print(tupla_resultado)
