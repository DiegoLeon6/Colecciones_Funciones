agenda = {}

entrada1 = input("Contacto 1 (Nombre - Teléfono): ")
entrada2 = input("Contacto 2 (Nombre - Teléfono): ")

def procesar(entrada):
    partes = entrada.split("-")
    nombre = partes[0].strip()
    telefono = partes[1].strip()
    return nombre, telefono

n1, t1 = procesar(entrada1)
n2, t2 = procesar(entrada2)

agenda[n1] = t1
agenda[n2] = t2


print(agenda)

