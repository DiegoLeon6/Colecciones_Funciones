def celsius_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Ingrese la temperatura en Celsius: "))
f = celsius_fahrenheit(c)
print("Temperatura en Fahrenheit:", f)

