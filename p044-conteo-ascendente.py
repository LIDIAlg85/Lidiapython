# p044-conteo-ascendente.py
#Imprimir los números de 1 a 100 usando  while

print("\033[2J\033[H")
print(" Imprime los números de 1 a 100 usando  while")

n=int(input('hasta donde ? '))
m=int(input('Incrementos ? '))

c = 1
while c <= n :
  print(f" {c}", end="")
  c += m
print("\n  proseso terminado")