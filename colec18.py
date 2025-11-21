# Pedir datos
c1 = input("Estudiante 1 (Nombre: Nota): ")
c2 = input("Estudiante 2 (Nombre: Nota): ")
c3 = input("Estudiante 3 (Nombre: Nota): ")

# Diccionario donde guardaremos las notas
notas = {}

# Procesar el contacto 1
nombre1, nota1 = c1.split(":")
notas[nombre1.strip()] = float(nota1.strip())

# Procesar el contacto 2
nombre2, nota2 = c2.split(":")
notas[nombre2.strip()] = float(nota2.strip())

# Procesar el contacto 3
nombre3, nota3 = c3.split(":")
notas[nombre3.strip()] = float(nota3.strip())

# Calcular promedio
promedio = sum(notas.values()) / len(notas)

print("Promedio general:", promedio)
