
def invertir(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return invertir(cadena[1:]) + cadena[0]

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "") 
    return cadena == invertir(cadena)

texto = input("Ingrese una cadena: ")
if es_palindromo(texto):
    print("Es palíndromo")
else:
    print("No es palíndromo")

