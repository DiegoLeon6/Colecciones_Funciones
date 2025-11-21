def invertir(cadena):
    if len(cadena) == 0:  # Caso base: cadena vacía
        return ""
    else:
        return invertir(cadena[1:]) + cadena[0]  # Llamada recursiva

texto = input("Ingrese una cadena: ")
print("Cadena invertida:", invertir(texto))

