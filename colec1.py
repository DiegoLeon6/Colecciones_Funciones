numeros = input("Ingrese números separados por espacios: ").split()

lista = []
for n in numeros:
    lista.append(int(n))

promedio = sum(lista) / len(lista)

mayores = []
for n in lista:
    if n > promedio:
        mayores.append(n)

print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)

