# p018-area-volumen -cilindro.py
# Crea un programa que calcule el área y volumen de un cilindro


import math as mt
print("\033[2J\033[1;1H",end="")

radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

area = 2 * mt.pi * radio * (radio + altura)
volume = mt.pi * radio**2 * altura

print(f"\nEl área del cilindro es: {area:.2f}")
print(f"El volumen del cilindro es: {volume:.2f}")

