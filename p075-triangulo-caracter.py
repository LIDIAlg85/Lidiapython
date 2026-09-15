#p075-triangulo-caracter.py
# Dibuja un cuadro del caracter deseado
print('\033[H\033[J')
print ('--- Dibuja un cuadro de caracteres ---\n')

r = 5
car = '*'

for i in range(1, r + 1):

  for j in range(1, r + 1):

    print('*', end="")

print()