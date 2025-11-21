numeros = input("Ingrese números separados por espacios: ").split()

# Convertir a enteros
lista = []
for n in numeros:
    lista.append(int(n))

# Calcular promedio
promedio = sum(lista) / len(lista)

# Buscar mayores que el promedio
mayores = []
for n in lista:
    if n > promedio:
        mayores.append(n)

print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)
