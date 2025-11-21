
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))


print("Ingrese los valores de la matriz:")
M = []
for i in range(filas):
    fila = input(f"Fila {i+1}: ").split()
    fila_num = []
    for n in fila:
        fila_num.append(int(n))
    M.append(fila_num)


T = []
for j in range(columnas):
    fila_trans = []
    for i in range(filas):
        fila_trans.append(M[i][j])
    T.append(fila_trans)

print("Matriz transpuesta:")
print(T)

