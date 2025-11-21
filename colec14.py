# Ingresar conjunto A
entradaA = input("Ingrese los elementos del conjunto A separados por espacio: ").split()
A = set(int(x) for x in entradaA)

# Ingresar conjunto B
entradaB = input("Ingrese los elementos del conjunto B separados por espacio: ").split()
B = set(int(x) for x in entradaB)

# Diferencia simétrica (elementos que están en solo uno)
dif_sim = A ^ B  # También se puede usar: A.symmetric_difference(B)

# Mostrar resultado
print(dif_sim)
