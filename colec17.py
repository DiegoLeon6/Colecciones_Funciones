frase = input("Ingrese una frase: ")

palabras = frase.split()      # Separar por espacios
conteo = {}                   # Diccionario vacío

for palabra in palabras:
    if palabra in conteo:     # Si ya existe en el diccionario
        conteo[palabra] += 1  # Incrementar el contador
    else:
        conteo[palabra] = 1   # Primera vez que aparece

print(conteo)
