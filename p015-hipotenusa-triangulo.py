# p015-hipotenusa-triangulo.py
# Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo


import math as mt
print("\033[2J\033[1;1H",end="")


print("--- Calculador de Hipotenusa ---")

lado1 = float(input("Ingresa la longitud del primer cateto: "))
lado2 = float(input("Ingresa la longitud del segundo cateto: "))


hipotenusa = mt.sqrt(lado1**2 + lado2**2)

print(f"\nLa longitud de la hipotenusa es: {hipotenusa:.2f}")

