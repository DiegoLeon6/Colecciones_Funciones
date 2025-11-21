n = int(input("Ingrese el tamaño de la matriz identidad: "))

# Crear la matriz identidad
matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

# Mostrar la matriz
for fila in matriz:
    print(fila)
