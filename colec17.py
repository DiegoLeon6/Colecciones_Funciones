frase = input("Ingrese una frase: ")

palabras = frase.split()      
conteo = {}                  

for palabra in palabras:
    if palabra in conteo:    
        conteo[palabra] += 1 
    else:
        conteo[palabra] = 1 

print(conteo)

