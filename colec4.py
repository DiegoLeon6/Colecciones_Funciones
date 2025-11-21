
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))


print("Ingrese los valores de la matriz A:")
A = []
for i in range(filas):
    fila = input(f"Fila {i+1}: ").split()
    fila_num = []
    for n in fila:
        fila_num.append(int(n))
    A.append(fila_num)


print("Ingrese los valores de la matriz B:")
B = []
for i in range(filas):
    fila = input(f"Fila {i+1}: ").split()
    fila_num = []
    for n in fila:
        fila_num.append(int(n))
    B.append(fila_num)

S = []
for i in range(filas):
    fila_suma = []
    for j in range(columnas):
        fila_suma.append(A[i][j] + B[i][j])
    S.append(fila_suma)


print("Suma de las matrices:")
print(S)


