# Ingresar los números separados por espacios
entrada = input("Ingrese los números separados por espacio: ").split()

# Convertir a tupla de enteros
tupla = tuple(int(num) for num in entrada)

# Calcular suma y promedio
suma_total = sum(tupla)
promedio = suma_total / len(tupla)

# Mostrar resultados
print("Suma =", suma_total)
print("Promedio =", promedio)
