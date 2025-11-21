
entradaA = input("Ingrese los elementos del conjunto A separados por espacio: ").split()
A = set(int(x) for x in entradaA)


entradaB = input("Ingrese los elementos del conjunto B separados por espacio: ").split()
B = set(int(x) for x in entradaB)


union = A | B          # Unión
diferencia = A - B     # Diferencia

print("Unión:", union)
print("Diferencia:", diferencia)

