
entradaA = input("Ingrese los números de la lista A separados por espacio: ").split()
A = [int(x) for x in entradaA]


entradaB = input("Ingrese los números de la lista B separados por espacio: ").split()
B = [int(x) for x in entradaB]


setA = set(x for x in A if x % 2 == 0)
setB = set(x for x in B if x % 2 == 0)


pares_comunes = setA & setB


print(pares_comunes)

