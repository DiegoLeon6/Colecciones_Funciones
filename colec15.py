
entradaA = input("Ingrese los elementos del conjunto A separados por espacio: ").split()
A = set(int(x) for x in entradaA)


entradaB = input("Ingrese los elementos del conjunto B separados por espacio: ").split()
B = set(int(x) for x in entradaB)


if A.issubset(B):
    print("A es subconjunto de B")
else:
    print("A NO es subconjunto de B")


if B.issuperset(A):
    print("B es superconjunto de A")
else:
    print("B NO es superconjunto de A")

