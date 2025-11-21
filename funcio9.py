def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print("Resultado:", potencia(b, e))

