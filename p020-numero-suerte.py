# p020-numero-suerte.py
# Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos
  ## Mostrar cada uno de los dígitos individuales del año. 
  ## Calcular y mostrar la suma de los dígitos individuales del año. 

import math as mt
print("\033[2J\033[1;1H",end="")

año_str = input("Introduce tu año de nacimiento (4 dígitos): ")


digitos = [int(d) for d in año_str]


print("Dígitos individuales:", *digitos)


suma_digitos = sum(digitos)
print(f"Suma de los dígitos: {suma_digitos}")














  





