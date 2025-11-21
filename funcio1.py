def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

# Ejemplo de uso:
numero = int(input("Ingrese un número: "))
print(factorial(numero))
