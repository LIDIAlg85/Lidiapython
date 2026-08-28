# p039-numeros-romanos.py
# Escribe un programa que reciba un número entero del 1 al 10 y muestre su equivalente en números romanos.
# Si el número está fuera de rango, mostrar error.


print("\033[2J\033[H")
num = int(input("Ingrese un número del 1 al 10: "))

if num == 1:
    print("El número romano es: I")
elif num == 2:
    print("El número romano es: II")
elif num == 3:
    print("El número romano es: III")
elif num == 4:
    print("El número romano es: IV")
elif num == 5:
    print("El número romano es: V")
elif num == 6:
    print("El número romano es: VI")
elif num == 7:
    print("El número romano es: VII")
elif num == 8:
    print("El número romano es: VIII")
elif num == 9:
    print("El número romano es: IX")
elif num == 10:
    print("El número romano es: X")
else:
    print("Error: el número ingresado está fuera del rango permitido.")