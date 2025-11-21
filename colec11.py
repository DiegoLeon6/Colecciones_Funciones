# Ingresar conjunto A
entradaA = input("Ingrese los elementos del conjunto A separados por espacio: ").split()
A = set(int(x) for x in entradaA)

# Ingresar conjunto B
entradaB = input("Ingrese los elementos del conjunto B separados por espacio: ").split()
B = set(int(x) for x in entradaB)

# Operaciones con conjuntos
union = A | B          # Unión
diferencia = A - B     # Diferencia

# Resultados
print("Unión:", union)
print("Diferencia:", diferencia)
