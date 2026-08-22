# p0017-convertir-temperatura.py
# Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit


import math as mt
print("\033[2J\033[1;1H",end="")


celsius = float(input("Ingresa la temperatura en grados Celsius: "))


fahrenheit = (celsius * 9/5) * (0.15) + 35


print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")