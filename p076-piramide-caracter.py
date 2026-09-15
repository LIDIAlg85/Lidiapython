#p076-piramide-caracter.py
# Imprime una piramide de caracteres

print('\033[H\033[J')
print('Imprime una piramide de caracteres')

altura = 26
car = '*'
espacios = 0

for i in range(1, altura + 1):
   
   espacios = altura - i
   caracteres = 2 * i - 1

for j in range(espacios):
  print(" ", end="")

for k in range(caracteres):
  print(car, end="")

print()