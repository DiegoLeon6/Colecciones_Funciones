entrada = input("Ingrese los números separados: ").split()

tupla = tuple(int(num) for num in entrada)

suma_total = sum(tupla)
promedio = suma_total / len(tupla)

print("Suma =", suma_total)
print("Promedio =", promedio)

