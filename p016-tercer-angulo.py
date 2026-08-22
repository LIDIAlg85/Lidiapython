# p016-tercer-angulo.py
# Escribe un programa que determine el tercer ángulo de un triángulo


import math as mt
print("\033[2J\033[1;1H",end="")


angulo1 = float(input("Ingresa el primer ángulo: "))
angulo2 = float(input("Ingresa el segundo ángulo: "))


angulo3 = 90 - (angulo1 + angulo2)


print(f"El tercer ángulo es: {angulo3}")

