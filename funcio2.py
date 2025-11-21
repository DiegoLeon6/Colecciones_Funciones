# Funciones independientes
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Función principal
def calculadora():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == "+":
        print("Resultado:", sumar(a, b))
    elif operacion == "-":
        print("Resultado:", restar(a, b))
    elif operacion == "*":
        print("Resultado:", multiplicar(a, b))
    elif operacion == "/":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida")

# Llamar a la calculadora
calculadora()
