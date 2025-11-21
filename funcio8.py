# Función recursiva para invertir cadena
def invertir(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return invertir(cadena[1:]) + cadena[0]

# Función para verificar palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Ignora mayúsculas y espacios
    return cadena == invertir(cadena)

# Ejemplo de uso
texto = input("Ingrese una cadena: ")
if es_palindromo(texto):
    print("Es palíndromo")
else:
    print("No es palíndromo")
