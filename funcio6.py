def contar_digitos(n):
    return len(str(abs(n)))  # Convierte a string y cuenta los caracteres

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
print("Cantidad de dígitos:", contar_digitos(numero))
