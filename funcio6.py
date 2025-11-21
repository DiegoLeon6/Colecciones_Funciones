def contar_digitos(n):
    return len(str(abs(n))) 

numero = int(input("Ingrese un número: "))
print("Cantidad de dígitos:", contar_digitos(numero))


