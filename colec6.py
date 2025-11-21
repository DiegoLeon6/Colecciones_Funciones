entrada = input("Ingresa los elementos separados por comas: ")

lista = [x.strip() for x in entrada.split(",")]

tupla_resultado = tuple(set(lista))

print(tupla_resultado)

