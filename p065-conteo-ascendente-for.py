# p065-conteo-ascendente-for.py
## Escribe un programa que utilice un ciclo for para mostrar en pantalla una secuencia ascendente.


print('\033[H\033[J')

print(" Iniciando secuencia de conteo ascendente...")

for i in range(1, 101, 1):
  print(i, end=' ')

