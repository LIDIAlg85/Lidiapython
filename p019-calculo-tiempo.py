# p019 calculando-tiempo.py
# Diseña un programa que tome una cantidad de horas como un número entero


import math as mt
print("\033[2J\033[1;1H",end="")

horas = int(input("Ingresa la cantidad de horas: "))


dias = horas / 24
minutos = horas * 60
segundos = minutos * 60



print(f"\n{horas} horas equivalen a:")
print(f" {dias:.2f} días")
print(f" {minutos:,} minutos")
print(f" {segundos:,} segundos")




