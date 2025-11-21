
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def mcm(a, b):
    return abs(a * b) // mcd(a, b)

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

print("MCD:", mcd(x, y))
print("MCM:", mcm(x, y))

