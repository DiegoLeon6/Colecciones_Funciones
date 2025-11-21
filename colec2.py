
listaA = input("Ingrese la lista A (números separados por espacios): ").split()
listaB = input("Ingrese la lista B (números separados por espacios): ").split()

A = []
for n in listaA:
    A.append(int(n))

B = []
for n in listaB:
    B.append(int(n))

producto_escalar = 0
for i in range(len(A)):
    producto_escalar += A[i] * B[i]

print("Producto escalar:", producto_escalar)

