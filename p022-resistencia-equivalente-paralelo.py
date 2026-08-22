# p022-resistencia- equivalente-paralelo.py
#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo. 
## Rt = 1/ ((1/R1)+(1/R2)+(1/R3))

import math as mt
print("\033[2J\033[1;1H",end="")



print("Calculadora de Resistencia Equivalente en Paralelo (4 Resistencias)")
print("-" *10)


r1 = float(input("Ingrese el valor de la resistencia R1 (en ohms): "))
r2 = float(input("Ingrese el valor de la resistencia R2 (en ohms): "))
r3 = float(input("Ingrese el valor de la resistencia R3 (en ohms): "))
r4 = float(input("Ingrese el valor de la resistencia R4 (en ohms): "))


if r1 <= 0 or r2 <= 0 or r3 <= 0 or r4 <= 0:
    print("Error: Los valores de las resistencias deben ser mayores a cero.")

else:
    
    inversos = 1 / ((1 / r1) + (1 / r2) + (1 / r3) + (1 / r4))
    

    # Mostrar el resultado final en pantalla
    print("-" *10)
    print(f"La resistencia total equivalente (Rt) es: {inversos:.2f} ohms")

   