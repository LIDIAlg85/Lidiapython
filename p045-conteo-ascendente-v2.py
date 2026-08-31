# p045-conteo-ascendente-v2.py
# Imprime los números de 1 a n, en incrementos de m, usando un ciclo while

print("\033[2J\033[H")
print(" Imprime los números de 1 a n usando  while")

n=int(input('hasta donde ? '))
m=int(input('Incrementos ? '))

c = 1
while c <= n :
  print(f" {c}", end="")
  c += m
print("\n  proseso terminado")