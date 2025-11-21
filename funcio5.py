def maximo_de_tres(a, b, c):
    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    return maximo

# Ejemplo de uso
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
z = float(input("Ingrese el tercer número: "))

print("El número mayor es:", maximo_de_tres(x, y, z))
