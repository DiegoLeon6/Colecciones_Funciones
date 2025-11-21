
a1 = input("A - Par 1 (clave: valor): ")
a2 = input("A - Par 2 (clave: valor): ")

A = {}
c1, v1 = a1.split(":")
A[c1.strip()] = v1.strip()

c2, v2 = a2.split(":")
A[c2.strip()] = v2.strip()


b1 = input("B - Par 1 (clave: valor): ")
b2 = input("B - Par 2 (clave: valor): ")

B = {}
c3, v3 = b1.split(":")
B[c3.strip()] = v3.strip()

c4, v4 = b2.split(":")
B[c4.strip()] = v4.strip()

# Fusionar
A.update(B)

print(A)

