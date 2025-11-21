# Ingresar lista A
entradaA = input("Ingrese los números de la lista A separados por espacio: ").split()
A = [int(x) for x in entradaA]

# Ingresar lista B
entradaB = input("Ingrese los números de la lista B separados por espacio: ").split()
B = [int(x) for x in entradaB]

# Convertir a sets y filtrar solo pares
setA = set(x for x in A if x % 2 == 0)
setB = set(x for x in B if x % 2 == 0)

# Intersección de pares
pares_comunes = setA & setB

# Mostrar resultado
print(pares_comunes)
