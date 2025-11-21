
entradaA = input("Ingrese los elementos del conjunto A separados por espacio: ").split()
A = set(int(x) for x in entradaA)


entradaB = input("Ingrese los elementos del conjunto B separados por espacio: ").split()
B = set(int(x) for x in entradaB)


dif_sim = A ^ B  # También se puede usar: A.symmetric_difference(B)

print(dif_sim)

