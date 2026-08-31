# p051-adivina-numero.py
# Permitir adivinar un numero generado al azar entre 1 y 50

print("\033[2J\033[H")
print( 'Adivina el Número')
print("He pensado en un número entre 1 y 50. ¿adivina cual es?")

import random 

ns = random.randint(1, 50) 
ci = 0
while True:
 intento = int(input("Cual es? "))
 ci += 1
 if intento < ns:
  print("Demasiado bajo Intenta con un número más alto")
 elif intento> ns:
  print( "Demasiado alto Intenta con un número más bajo.")
 else:
  print(f"\nFelicidades Adivinaste el número en ")
  print(f"El numero era:",ns)