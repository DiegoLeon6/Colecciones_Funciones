
x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))

coordenada = (x, y)

limite_inferior = int(input("Límite inferior del rango: "))
limite_superior = int(input("Límite superior del rango: "))

if limite_inferior <= coordenada[0] <= limite_superior and \
   limite_inferior <= coordenada[1] <= limite_superior:
    print("Dentro del rango")
else:
    print("Fuera del rango")

