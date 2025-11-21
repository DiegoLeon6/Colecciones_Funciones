
a1, a2, a3 = input("Primer número de la tupla 1: "), input("Segundo número: "), input("Tercer número: ")
tupla1 = (int(a1), int(a2), int(a3))

b1, b2, b3 = input("Primer número de la tupla 2: "), input("Segundo número: "), input("Tercer número: ")
tupla2 = (int(b1), int(b2), int(b3))

if tupla1 > tupla2:
    print("La primera tupla es mayor.")
elif tupla1 < tupla2:
    print("La segunda tupla es mayor.")
else:
    print("Las tuplas son iguales.")

