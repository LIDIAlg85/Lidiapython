# p023-verificar-numero.py
#Verificar si un número entero es positivo, negativo o cero.

print("\033[2J\033[1;1H",end="")
print('Verificar si un numero es positivo, negativo o cero')

numero = int(input('Dame un numero entero ? '))

if numero > 0:
   print('El numero es POSITIVO 👍')
if numero < 0:
   print('El numero es NEGATIVO +👎')
if numero == 0:
   print('El numero es CERO 🤷‍♀️')

print('\nAqui ya terminamos de tomar decisiones')