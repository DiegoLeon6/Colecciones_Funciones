
p1 = input("Par 1 (clave: valor): ")
p2 = input("Par 2 (clave: valor): ")
p3 = input("Par 3 (clave: valor): ")


original = {}


c1, v1 = p1.split(":")
original[c1.strip()] = v1.strip()

c2, v2 = p2.split(":")
original[c2.strip()] = v2.strip()

c3, v3 = p3.split(":")
original[c3.strip()] = v3.strip()


invertido = {}

for clave, valor in original.items():
    invertido[valor] = clave

print(invertido)

