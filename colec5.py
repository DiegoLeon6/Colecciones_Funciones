# Ingresar tamaño de la matriz
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

# Ingresar la matriz
print("Ingrese los valores de la matriz:")
M = []
for i in range(filas):
    fila = input(f"Fila {i+1}: ").split()
    fila_num = []
    for n in fila:
        fila_num.append(int(n))
    M.append(fila_num)

# Crear matriz transpuesta
T = []
for j in range(columnas):
    fila_trans = []
    for i in range(filas):
        fila_trans.append(M[i][j])
    T.append(fila_trans)

# Mostrar resultado
print("Matriz transpuesta:")
print(T)
